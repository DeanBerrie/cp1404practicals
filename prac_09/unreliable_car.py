"""
CP1404 Prac09
unreliable car
Dean Berrie
"""

from car import Car
import random


class UnreliableCar(Car):
    """Creates an unreliable car class"""

    def __init__(self, name, fuel, reliability: float):
        """Constructs a unreliable car class."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car based on reliability"""
        random_number = random.randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
