###
### Author: Pranav I Anilkumar  
### Class: CSc 110
### Description: A program that can print out three shapes; an hourglass, a plumbbob, a house
###              according to two inputs from the user the row hieght and the character string. 
###

import os 

def row(number):
    '''
    This is a a function for the row '|---------|'
    '''

    print('|---------|\n' * number, end='')

def down_arrow(charchter_string):
    '''
    This is a fuction for downward arrow 
    '''

    print(charchter_string * 11)
    print(' '+charchter_string * 9)
    print('  '+charchter_string * 7)
    print('   '+charchter_string * 5)  
    print('    '+charchter_string * 3)
    print('     '+charchter_string)   


def up_arrow(charchter_string):
    '''
    This is a fuction for upward arrow or roof 
    '''

    print('     '+charchter_string) 
    print('    '+charchter_string * 3)
    print('   '+charchter_string * 5)
    print('  '+charchter_string * 7)
    print(' '+charchter_string * 9)
    print(charchter_string * 11)

def main():
    '''
    This is the main fuction where the user input is recieved and
    and the required output is printed out.
    '''

    shape_type_  = input('Enter shape to display:\n')
    arrow_charachter = input('Enter arrow character:\n')
    row_height = int(input('Enter row-area height:\n'))
    print()

    if shape_type_ == 'house':
        up_arrow(arrow_charachter)
        row(row_height)
    
    elif shape_type_ == 'plumbbob':
        up_arrow(arrow_charachter)
        row(row_height)
        down_arrow(arrow_charachter)
    
    elif shape_type_ == 'hourglass':
        row(row_height)
        down_arrow(arrow_charachter)
        up_arrow(arrow_charachter)
        row(row_height)

main()
os._exit