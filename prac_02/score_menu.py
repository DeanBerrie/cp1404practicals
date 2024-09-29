"""
CP1404 - Prac 2
Score Menu
"""
from score import determine_score_category

MENU = "(G)et valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    score = get_valid_score()
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "G":
            score = get_valid_score()
        elif menu_choice == "P":
            print_result(score)
        elif menu_choice == "S":
            show_stars(score)
        else:
            print("Invalid")
        print(MENU)
        menu_choice = input(">>> ").upper()
    print("The program will now quit")


def print_result(score):
    """print score and score category"""
    score_category = determine_score_category(score)
    print(f'The score {score} is {score_category}')


def get_valid_score():
    """get a valid score between 0-100"""
    score = int(input("Score: "))
    while score > 100 or score < 0:
        print("Invalid")
        score = int(input("Score: "))
    return score


def show_stars(score):
    print(score * "*")


main()
