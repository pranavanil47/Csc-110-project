'''
this is a program  to calculate the pythogorus theorm 
using the def function
'''
import math

def pythg(side1, side2):
    side1 = side1 ** 2
    side2 = side2 ** 2
    to_root = side1 + side2

    hyp = to_root ** (1/2)
    return hyp



number = (input('No of triangles  to calculate '))
if number.isnumeric() == False:
    print('Enter a positive integer for number')
    
else:
    number = int(number)
    i = 0
    while i < number:
        s1 = (input('Enter side 1 '))
        s2 = (input('Enter side 2 '))
        i +=1

        if s1.isnumeric()  == False or s2.isnumeric() == False:
            print('enter a positive value')
            

        else:
            hypotnuse = pythg(float(s1), float(s2))
            print(hypotnuse)
  

