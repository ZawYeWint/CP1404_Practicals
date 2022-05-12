from taxi import Taxi

def main():
    # Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km
    taxi = Taxi("Prius 1", 100, 1.23)

    # Drive the taxi 40 km
    taxi.drive(40)

    # Print the taxi's details and the current fare
    print(taxi)
    print(f"Current fare: ${taxi.get_fare():.2f}")

    # Restart the meter (start a new fare) and then drive the car 100 km

    # Print the details and the current fare

if __name__ == '__main__':
    main()