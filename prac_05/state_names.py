"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

STATE_CODE_TO_STATE = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory",
                       "WA": "Western Australia",
                       "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania",
                       "SA": "South Australia"}
print(STATE_CODE_TO_STATE)

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", STATE_CODE_TO_STATE[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

for state in STATE_CODE_TO_STATE:
    print(f'{state:3} is {STATE_CODE_TO_STATE[state]}')
