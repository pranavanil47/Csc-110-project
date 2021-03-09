###
### Author : Pranav I Anilkumar
### Class : CSc 110
### Description : A program that prints out center alligned '#' signs according to the specific
###               digits of a string input given by the user.    
###
### (note - this program fails if the input has uneven number of digits or if the input is not an integer)




bars = input('Enter bar string:\n')

print('+------------------+')

index = 0 

while index <= len(bars)-1:                 ###looping 
    first_num = int(bars[index])
    second_num = int(bars[index + 1]) 
    print('|' +' '* (9 -first_num )+'#'* first_num+'#'*second_num+' ' * (9-second_num)+'|') ##here the total size of the bars is 20 characters
                                                                                            ## 10 on each side
    index+= 2                                                              ### As i used index + 1 to skip odd character strings i added 2 to loop

print('+------------------+')