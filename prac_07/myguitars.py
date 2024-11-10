from guitar import Guitar
from operator import itemgetter

def main():
    guitars = []
    with open('guitars.csv', "r", encoding="utf-8-sig") as infile:
        for line in infile:
            parts = line.strip().split(",")
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    for guitar in sorted(guitars):
        print(guitar)


main()
