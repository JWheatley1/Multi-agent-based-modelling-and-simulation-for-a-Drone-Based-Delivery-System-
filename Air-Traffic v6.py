from mesa.time import RandomActivation
from mesa import Model,Agent
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
import random

class Aircraft(Agent):
    def __init__(self,unique_id, model, origin, destination:
        super().__init__(unique_id, model)
        self.origin = origin
        self.destination = destination
        self.speed = random.uniform(200, 600)
        self.altitude = random.uniform(3000, 40000)
        self.route = None

    def step(self):
        if not self.destination:
            self.destination = random.choice(self.model.airports)

        x, y = self.position
        dest_x, dest_y = self.destination.position

        dx = dest_x - x
        dy = dest_y - y

        dist = (dx **2 + dy **2) ** 0.5

        if dist <= self.speed:
            self.position = self.destination.position
            self.destination = None
        else:
            move_x = dx * (self.speed / dist)
            move_y = dy * (self.speed / dist)
            new_x = x + move_x
            new_y = y + move_y

        self.postion = (new_x, new_y)

class Airport(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.position = (random.randint(0,100), random.randint(0,100))
        self.agents_in_airport = []

    def step(self):
        pass

class AirTraffic(Model):
    def __init__(self, num_aircraft, num_airports):
        self.num_aircraft = num_aircraft
        self.num_airports = num_airports
        self.schedule = RandomActivation(self)
        self.grid


