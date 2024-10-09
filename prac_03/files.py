# 1
def question_1():
    input_name = input("Name: ")
    out_file = open('name.txt', 'w')
    print(input_name, file=out_file)
    out_file.close()


# 2
def question_2():
    infile = open('name.txt', 'r')
    read_name = infile.read()
    print(f'Hi {read_name.strip()}!')
    infile.close()


# 3
def question_3():
    with open('numbers.txt', "r") as infile:
        first_number = int(infile.readline())
        second_number = int(infile.readline())
        final_number = first_number + second_number
        print(final_number)


# 4
def question_4():
    total = 0
    with open('numbers.txt', 'r') as infile:
        for line in infile:
            number = int(line)
            total = total + number
        print(f'The total of all numbers are {total}')


question_1()
question_2()
question_3()
question_4()
