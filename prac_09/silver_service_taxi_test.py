"""
CP1404 Prac09
Silver service taxi tests
Dean Berrie
"""

from silver_service_taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Taxi-test", 100, 2)
    taxi.drive(18)
    print(taxi)
    assert taxi.get_fare() == 48.78
    print(taxi.get_fare())


main()
