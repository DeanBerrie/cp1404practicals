input_name = input("Name: ")
out_file = open('name.txt', 'w')
print(input_name, file=out_file)
out_file.close()

infile = open('name.txt', 'r')
read_name = infile.read()
print(f'Hi {read_name.strip()}!')
