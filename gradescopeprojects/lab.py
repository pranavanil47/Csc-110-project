###
### Author : Pranav I Anilkumar
### Class : CSc 110
### Description : A program that prints out left alligned '#' signs according to the specific
###               digits of a string input given by the user.    
###(note - this program fails if the input is not an integer)



bars = input('Enter bar string:\n')
index = 0
print('+'+'-' * 9+'+')                              ### here the total size of the bars is 11 characters

while index <= len(bars)-1:                                     ###looping 
    print('|'+'#' * int(bars[index])+' ' *(9- int(bars[index]) ) +'|')
    index += 1

print('+'+'-' * 9+'+')


