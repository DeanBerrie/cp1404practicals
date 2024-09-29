"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    user_score = float(input("Enter score: "))
    while user_score > 100 or user_score < 0:
        print("Invalid Score")
        score = float(input("Enter score: "))

    user_score_category = determine_score_category(user_score)
    print(user_score_category)
    random_score = random.randint(0, 100)
    random_score_category = determine_score_category(random_score)
    print(f'Random score: {random_score}')
    print(f'Random score category: {random_score_category}')


def determine_score_category(score):
    """determine if score is bad, passable, or excellent"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


if __name__ == "__main__":
    main()