###
### Author: Pranav I Anilkumar  
### Class: CSc 110
### Description: A program that can print out the factorial of an integer given by the user.  
###               

import os 

number = int(input('Enter factorial to calculate:\n'))

index = 1
factorial = 1
while index <= number:
    factorial *=index                 ### creating a loop which keeps on multiplying the factorial
    index += 1                        #### until the number input is reached.
print('')
print(number, 'factorial =', factorial)
os._exit