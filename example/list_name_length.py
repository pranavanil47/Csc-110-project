def print_name_(names):
    i = 0
    while i<len(names):
        print(len(names[i]))
        i += 1

names= input('enter name')
name_list = names.split(' ')

print_name_(name_list)