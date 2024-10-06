"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? A value error will occur when a non-integer value has been entered for either numerator
or denominator
2. When will a ZeroDivisionError occur? A Zero division error occurs when the denominator is equal to zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError? You could add a while loop saying that
while denominator is equal to zero it will keep asking for another denominator until it is no longer zero
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
