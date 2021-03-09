## to check both weight and age to get inside a rollercoast

age = int(input('Enter age\n'))
wght = int(input('Enter weight in lbs\n'))
print('')
if 18 <= age <= 65:
    if 100 <= wght <= 300:
        print('You are allowed inside the rides')
    else:
        print('Not allowed')


else:
    print('Not allowed')