def sum():
    number_file = open('numbers1.txt', 'r')
    value = 0
    for line in number_file:
        value += int(line)
    print(value)

sum()