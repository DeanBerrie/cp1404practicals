"""CP1404 Prac 2 - Password Stars"""
MINIMUM_PASSWORD_LENGTH = 8


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print(len(password) * '*')


def get_password():
    password = input("Password: ")
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print("Invalid. Password needs 8 characters minimum")
        password = input("Password: ")
    return password


main()
