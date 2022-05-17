from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """Initialising an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability
