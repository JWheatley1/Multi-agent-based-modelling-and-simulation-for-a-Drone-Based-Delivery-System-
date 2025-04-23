
import gurobipy as gp
from gurobipy import GRB



demand = [15, 18, 14, 20]


capacity = [20, 22, 17, 19, 18]


fixedCosts = [12000, 15000, 17000, 13000, 16000]
maxFixed = max(fixedCosts)
minFixed = min(fixedCosts)


transCosts = [[4000, 2000, 3000, 2500, 4500],
              [2500, 2600, 3400, 3000, 4000],
              [1200, 1800, 2600, 4100, 3000],
              [2200, 2600, 3100, 3700, 3200]]


plants = range(len(capacity))
warehouses = range(len(demand))

m = gp.Model('multiscenario')

open = m.addVars(plants,
                 vtype=GRB.BINARY,
                 obj=fixedCosts,
                 name="open")


transport = m.addVars(warehouses, plants, obj=transCosts, name="trans")


m.ModelSense = GRB.MINIMIZE

m.addConstrs(
    (transport.sum('*', p) <= capacity[p]*open[p] for p in plants),
    "Capacity")



demandConstr = m.addConstrs(
    (transport.sum(w) == demand[w] for w in warehouses), "Demand")


m.NumScenarios = 7

m.Params.ScenarioNumber = 0
m.ScenNName = 'Base model'


m.Params.ScenarioNumber = 1
m.ScenNName = 'Increased warehouse demands'
for w in warehouses:
    demandConstr[w].ScenNRhs = demand[w] * 1.1


m.Params.ScenarioNumber = 2
m.ScenNName = 'Double the warehouse demands'
for w in warehouses:
    demandConstr[w].ScenNRhs = demand[w] * 2.0


m.Params.ScenarioNumber = 3
m.ScenNName = 'Decreased plant fixed costs'
for p in plants:
    open[p].ScenNObj = fixedCosts[p] * 0.95


m.Params.ScenarioNumber = 4
m.ScenNName = 'Increased warehouse demands and decreased plant fixed costs'
for w in warehouses:
    demandConstr[w].ScenNRhs = demand[w] * 1.1
for p in plants:
    open[p].ScenNObj = fixedCosts[p] * 0.95


m.Params.ScenarioNumber = 5
m.ScenNName = 'Force plant with largest fixed cost to stay open'
open[fixedCosts.index(maxFixed)].ScenNLB = 1.0

m.Params.ScenarioNumber = 6
m.ScenNName = 'Force plant with smallest fixed cost to be closed'
open[fixedCosts.index(minFixed)].ScenNUB = 0.0


m.write('multiscenario.lp')

for p in plants:
    open[p].Start = 1.0


p = fixedCosts.index(maxFixed)
open[p].Start = 0.0
print('Initial guess: Closing plant %d\n' % p)


m.Params.Method = 2

m.optimize()


for s in range(m.NumScenarios):
    m.Params.ScenarioNumber = s

    print('\n\n------ Scenario %d (%s)' % (s, m.ScenNName))

    
    if m.ScenNObjVal >= m.ModelSense * GRB.INFINITY:
        if m.ScenNObjBound >= m.ModelSense * GRB.INFINITY:
            
            print('\nINFEASIBLE')
        else:
            
            print('\nNO SOLUTION')
    else:
        print('\nTOTAL COSTS: %g' % m.ScenNObjVal)
        print('SOLUTION:')
        for p in plants:
            if open[p].ScenNX > 0.5:
                print('Plant %s open' % p)
                for w in warehouses:
                    if transport[w, p].ScenNX > 0:
                        print('  Transport %g units to warehouse %s' %
                              (transport[w, p].ScenNX, w))
            else:
                print('Plant %s closed!' % p)


print('\n\nSummary: Closed plants depending on scenario\n')
tableStr = '%8s | %17s %13s' % ('', 'Plant', '|')
print(tableStr)

tableStr = '%8s |' % 'Scenario'
for p in plants:
    tableStr = tableStr + ' %5d' % p
tableStr = tableStr + ' | %6s  %-s' % ('Costs', 'Name')
print(tableStr)

for s in range(m.NumScenarios):
    
    m.Params.ScenarioNumber = s

    tableStr = '%-8d |' % s

   
    if m.ScenNObjVal >= m.ModelSense * GRB.INFINITY:
        if m.ScenNObjBound >= m.ModelSense * GRB.INFINITY:
           
            print(tableStr + ' %-30s| %6s  %-s' %
                  ('infeasible', '-', m.ScenNName))
        else:
            
            print(tableStr + ' %-30s| %6s  %-s' %
                  ('no solution found', '-', m.ScenNName))
    else:
        for p in plants:
            if open[p].ScenNX > 0.5:
                tableStr = tableStr + ' %5s' % ' '
            else:
                tableStr = tableStr + ' %5s' % 'x'

        print(tableStr + ' | %6g  %-s' % (m.ScenNObjVal, m.ScenNName))