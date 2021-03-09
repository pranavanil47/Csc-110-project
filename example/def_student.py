

def check(points):
    if points > 90:
        print('senior')
    elif points > 60:
        print('junior')
    elif points > 30:
        print('sophmore')
    elif points >= 0:
        print('fresman')
    else:
        print('wtf dude')
        
students = int(input('Enter the number of students to check    '))

index = 1

while students >= index:
    unit = int(input('Enter unit for student ' + str(index)+ '  '))
    print ('student', index,'is')
    check(unit)
    index += 1
