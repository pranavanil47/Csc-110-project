#### to check if 3 stuffs are afforadable 
budget = float(input('Enter budget:  ')) 
a = float(input('Cost of item A:  '))
b = float(input('Cost of item B:  '))
c = float(input('Cost of item C:  '))

total = a + b + c 

if total <= budget:
    print('Affordable')

if budget < a and budget< b and budget < c :
    print('You cannot afford anything')
else:
    print('You can only afford one or two of these products ')
