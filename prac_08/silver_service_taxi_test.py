from silver_service_taxi import SilverServiceTaxi


def main():
    """Testing SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


if __name__ == '__main__':
    main()
