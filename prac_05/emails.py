"""
Emails
Prac - 05
"""

email_to_name = {}
email = input("Email: ")
while email != "":
    full_name = email.split("@")[0]
    parts_of_name = full_name.split(".")
    name = " ".join(parts_of_name).title()
    name_confirmation = input(f'Is your name {name}? (Y/N) ').upper()
    if name_confirmation != "Y" and name_confirmation != "":
        name = input("Name: ")
    email_to_name[email] = name
    email = input("Email: ")


for email, name in email_to_name.items():
    print(f'{name} ({email})')
