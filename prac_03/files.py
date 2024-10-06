# input_name = input("Name: ")
# out_file = open('name.txt', 'w')
# print(input_name, file=out_file)
# out_file.close()
#
# infile = open('name.txt', 'r')
# read_name = infile.read()
# print(f'Hi {read_name.strip()}!')
# infile.close()

# with open('numbers.txt', "r") as infile:
#     first_number = infile.readline()
#     second_number = infile.readline()
#     final_number = first_number + second_number
#     print(final_number) #TODO

total = 0
with open('numbers.txt', 'r') as number_infile:
    for line in number_infile:
        number = int(line)
        total = total + number
    print(f'The total of all numbers are {total}')

