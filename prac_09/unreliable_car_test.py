"""
CP1404 Prac09
Unreliable car tests
Dean Berrie
"""

from unreliable_car import UnreliableCar


def main():
    """Test unreliable cars"""

    reliable_car = UnreliableCar("BMW", 100, 90)
    unreliable_car = UnreliableCar("Suzuki Swift", 100, 13)

    for i in range(1, 12):
        print(f'Attempting to drive {i}km:')
        print(f'{reliable_car.name} drove {reliable_car.drive(i)}km')
        print(f'{unreliable_car.name} drove {unreliable_car.drive(i)}km')

    print(unreliable_car)
    print(reliable_car)

main()
