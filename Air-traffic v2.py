import math
import random


class Airport:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


class Plane:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.x = random.uniform(0, 100)
        self.y = random.uniform(0, 100)

    def calculate_distance(self, airport):
        return math.sqrt((self.x - airport.x) ** 2 + (self.y - airport.y) ** 2)

    def calculate_time(self, airport):
        distance = self.calculate_distance(airport)
        return distance / self.speed


def main():
    airports = [
        Airport("Heathrow", 10, 20),
        Airport("Birmingham Airport", 50, 30),
        Airport("Edinburgh Airport", 80, 90),
    ]

    plane = Plane("BA Boeing 737", speed=10)

    for airport in airports:
        distance = plane.calculate_distance(airport)
        time = plane.calculate_time(airport)
        print(f"{plane.name} is flying to {airport.name}.")
        print(f"Distance: {distance:.2f} units")
        print(f"Time taken: {time:.2f} time units")
        print("-----")
        plane.x = airport.x
        plane.y = airport.y


if __name__ == "__main__":
    main()
