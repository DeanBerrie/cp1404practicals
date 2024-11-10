from guitar import Guitar


def main():
    guitars = []
    get_guitars(guitars)

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f'{guitar} added.')
        name = input("Name: ")

    write_to_file(guitars)


def write_to_file(guitars):
    with open("guitars.csv", "w", encoding="utf-8-sig") as outfile:
        for guitar in sorted(guitars):
            print(guitar, file=outfile)


def get_guitars(guitars):
    with open('guitars.csv', "r", encoding="utf-8-sig") as infile:
        for line in infile:
            parts = line.strip().split(",")
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)


main()
