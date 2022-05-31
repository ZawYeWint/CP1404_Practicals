from taxi import Taxi


def main():
    # Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km
    taxi = Taxi("Prius 1", 100)

    # Drive the taxi 40 km
    taxi.drive(40)

    # Print the taxi's details and the current fare
    print(taxi)
    print(f"Current fare: ${taxi.get_fare():.2f}")
    print()

    # Restart the meter (start a new fare) and then drive the car 100 km
    taxi.start_fare()  # reset the current distance fare to 0
    print(f"Current fare: ${taxi.get_fare():.2f} before moving any new distance")
    distance_driven = taxi.drive(100)  # fuel left is 6 units (60km worth of distance) expected fare 1.23 * 60 = 73.80

    # Print the details and the current fare
    print(f"After attempting to drive another 100km, the actual distance is: {distance_driven} km")
    print(taxi)
    print(f"Current fare: ${taxi.get_fare():.2f}")


if __name__ == '__main__':
    main()
