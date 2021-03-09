###
### Author: Pranav I Anilkumar 
### Class: CSc 110
### Description: This program is prints out a target acccording too the user and also prints
###              out the hits in a graph 
###


import os
target_string = input('Hit string:\n')
while len(target_string) % 4 != 0 or len(target_string) < 3:     ### checking the input requirement for target string 
    print('Please provide a valid hit string.')
    target_string = input('Hit string:\n')
    

marker_string_ = input('Marker:\n')  
while len(marker_string_)!= 1:
    print('Please provide a valid marker.')                       ### checking the input requirement for marker string 
    marker_string_ = input('Marker:\n')

current_hit_x = int(target_string[0] + target_string[1])             ### making a starting cordinates 
current_hit_y = int(target_string[2] + target_string[3])    


i = 4    
index_row_ = 5                                                               ### creating loop 
while index_row_ >= -5:
    index_column_= -7 
    while index_column_<= 7:
        if current_hit_x == index_column_ and current_hit_y == index_row_:           ### hit requirement 
            print(marker_string_, end='')
            if i < len(target_string):
                current_hit_x = int(target_string[i] + target_string[i+1])
                current_hit_y = int(target_string[i+2] + target_string[i+3])
                i += 4
        elif index_column_ == 0:
            print('|', end='')
        elif index_row_ == 0:
            print('-', end='')
        else:
            print(' ', end='')
        index_column_ += 1
    print('')
    index_row_ -= 1
os._exit
            
### -2+3+4-1 


        
