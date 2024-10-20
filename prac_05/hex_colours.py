COLOUR_TO_HEX_CODE = {"Aqua": "#00ffff", "Fawn": "#e5aa70", "Keppel": "#3", "Linen": "#faf0e6", "Mantis": "#74c365",
                      "Orchid": "#da70d6", "Ruby": "#e0115f", "Sienna": "a0522d", "Teal": "#008080", "Zaffre": "0014a8"}

user_colour = input("Enter Colour: ").title()
while user_colour != "":
    try:
        print(user_colour, "is", COLOUR_TO_HEX_CODE[user_colour])
    except KeyError:
        print("Invalid colour")
    user_colour = input("Enter Colour: ").title()
