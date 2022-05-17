from car import Car
from random import randint


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """Initialising an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Generating a random number between 0 and 100,
        and only driving the car if that number is less than the car's reliability"""
        random_number = randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
