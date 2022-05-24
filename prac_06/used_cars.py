"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Tesla Z", 180)  # create a Car object with 180 units of fuel, odometer is 0
    my_car.drive(30)  # 180 - 30 = 150 (fuel = 150, odometer = 30)
    print("fuel =", my_car.fuel)  # 150
    print("odo =", my_car.odometer)  # 30
    print(my_car)  # gibberish? object at a certain address

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))  # first way of printing using format
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))  # second way of printing using format with obj

    print(f"Car {{{my_car.fuel}}} {{{my_car.odometer}}}")  # third way of printing using f string
    # {{ is escaping {, }} is escaping}

    print("==" * 25)
    print("~~ Limo ~~")
    # Create a new Car object called "limo" that is initialised with 100 units of fuel.
    limo = Car(name="My Limousine", fuel=100)  # Car(100)

    # Add 20 more units of fuel to this new car object using the add method.
    limo.add_fuel(20)  # .add_fuel(amount=100)

    # Print the amount of fuel in the car.
    print(f"Fuel={limo.fuel}")  # Expect Fuel=120

    # Attempt to drive the car 115 km using the drive method.
    distance_driven = limo.drive(115)  # Compare the actual distance driven

    # Print the car's odometer reading.
    print(f"Odometer after moving {distance_driven} km = {limo.odometer}")

    # Now add the __str__ method to the Car class in car.py.
    print(limo)  # Car, fuel=5, odometer=115 --> My Limousine, fuel=5, odometer=115


if __name__ == '__main__':
    main()
