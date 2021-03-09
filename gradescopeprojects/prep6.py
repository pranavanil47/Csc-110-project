###
### Author: Pranav I Anilkumar  
### Class: CSc 110
### Description: A program that can print out the state of water 
###              based on the temperature input given by the user 
###


temp = int(input('Temperature in fahrenheit:\n'))

if (temp<32):
    print('Ice')

if (32<=temp<212):
    print('Water')

if (temp>=212):
 print('Steam')