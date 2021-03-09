def collect_names():
    times = int(input('number of names to be stored '))
    name_string = '' 

    while times>0:
        user_input = input('Enter the names to store  ')
        name_string += ' '+user_input
        times -=1
    name_list = name_string.split(' ')
    name_list = name_list[1:]
    return name_list

def collect_age():
    a =collect_names()
    age_list =[]
    i = 0
    while i < len(a):
        age = int(input('Enter age of', a[i]))

        age_list.append(age)
        i+=1
    
    return age_list,a


def main():
    age,name = collect_age()

    print()

    print('-----------------------------------')
    print('--now enter the name to check age-- ')
    print('-----------------------------------')
    print()
    n = input('Enter name to check age in the database ')
    print('-----------------------------------')

    index = 0 
    i = 0
    while i<len(name):
        if name[i] == n:
            break
        index+=1
        i+=1
    age_print = str(age[index])

    print('The age of', n, 'is', age_print)
     

    

main()