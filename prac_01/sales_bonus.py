"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales >= 1000:
        bonus_rate = 0.15
    else:
        bonus_rate = 0.1
    bonus_amount = bonus_rate * sales
    print(f'You get a bonus of ${bonus_amount:.2f}')
    sales = float(input("Enter sales: $"))
print("Done.")
