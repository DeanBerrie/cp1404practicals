from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

MENU = 'q)uit, c)hoose taxi, d)rive'


def main():
    taxis = [[Taxi('Prius', 100, 1.23)], [SilverServiceTaxi('Limo', 100, 2.46)]
        , [SilverServiceTaxi('Hummer', 100, 4.92)]]
    print("Lets Drive")
    total_fare_cost = 0
    taxi_choice = ""
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            for i, taxi in enumerate(taxis):
                print(f'{i} - {taxi}')
            choose_taxi = int(input("Choose taxi: "))
            taxi_choice = taxis[choose_taxi]
        elif menu_choice == "d":
            if taxi_choice != "":
                distance = float(input("Drive how far?: "))
                taxi_choice.drive(distance)
                print(f'Your {taxi_choice.name} trip cost you ${taxi_choice.get_fare()}')
                total_fare_cost += taxi_choice.get_fare()
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")

        print(MENU)
        menu_choice = input(">>> ").lower()
    print(f'Total trip costs ${total_fare_cost}')

main()
