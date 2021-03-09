

def check(semester_units, total_units):
    if semester_units >= 12:
        print('full time')
    else:
        print('part time')
    
    if total_units > 90:
        print('Senior')
    elif total_units > 60:
        print('junior')
    elif total_units > 30:
        print('sophmore')
    else:
        print('freshman')


students = int(input('Enter the number of students to check    '))

index = 1

while students >= index:
    semester = int(input('semester unit:  '))
    total = int(input('Total units:  '))
    print ('student', index,'is')
    check(semester,total)
    index += 1