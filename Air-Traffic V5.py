# Import necessary libraries
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
import random

# Create an Aircraft agent
class Aircraft(Agent):
    def __init__(self, unique_id, model, origin, destination):
        super().__init__(unique_id, model)
        self.origin = origin
        self.destination = destination
        self.speed = random.uniform(200, 600)
        self.altitude = random.uniform(3000, 40000)
        self.route = None

    def step(self):
        # Define aircraft behavior (e.g., follow flight plan, respond to instructions)
        pass

# Create an Airport agent
class Airport(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def step(self):
        # Define airport behavior (e.g., handle arrivals and departures)
        pass

# Create the AirTrafficModel
class AirTrafficModel(Model):
    def __init__(self, width, height, num_aircraft, num_airports):
        self.num_aircraft = num_aircraft
        self.num_airports = num_airports
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.datacollector = DataCollector(
            agent_reporters={"Speed": "speed", "Altitude": "altitude"}
        )

        # Create aircraft agents
        for i in range(self.num_aircraft):
            origin = random.choice(self.schedule.agents)
            destination = random.choice(self.schedule.agents)
            aircraft = Aircraft(i, self, origin, destination)
            self.grid.place_agent(aircraft, origin.pos)
            self.schedule.add(aircraft)

        # Create airport agents
        for i in range(self.num_airports):
            airport = Airport(i, self)
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            self.grid.place_agent(airport, (x, y))
            self.schedule.add(airport)

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()

# Create and run the model
width = 10
height = 10
num_aircraft = 5
num_airports = 10

model = AirTrafficModel(width, height, num_aircraft, num_airports)
for i in range(10):
    model.step()
