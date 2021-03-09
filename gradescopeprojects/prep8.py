###
### Author: Pranav I Anilkumar  
### Class: CSc 110
### Description: A program that can print out the numbers in between 0 and the
###              number the user gives as an input(including both 0 and the input) 
###




import os

number = input('Enter a positive number:\n')

if (number.isnumeric() == False) or (int(number)< 0):  ### checking if the input is +ve 
    print('enter positive integer value')              ##   and if it's an integer
    os._exit

elif (number.isnumeric() == True )and (int(number) >= 0):
    number = int(number)
    index = 0                      ### using 0 to make the print start from 0
    print('')
    while index <= number:       ### making a loop statement so it prints out integer from 0 to the input
        print(index)

        index += 1
    os._exit 




