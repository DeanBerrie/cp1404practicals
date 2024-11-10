from guitar import Guitar


def main():
    guitars = []
    with open('guitars.csv', "r", encoding="utf-8-sig") as infile:
        for line in infile:
            parts = line.strip().split(",")
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f'{guitar} added.')
        name = input("Name: ")

    with open("guitars.csv", "w", encoding="utf-8-sig") as outfile:
        for guitar in sorted(guitars):
            print(guitar, file=outfile)


main()
