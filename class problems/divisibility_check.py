### to check divisibility by 3 and 2 
import os 
number = int(input('Enter value to be checked if divisible by 3 & 2:\n'))

div_2_ = number  % 2 
div_3_ = number  % 3
print('')
if number >= 3:
    if div_2_ == 0 and div_3_ == 0:
        print('Divisible by both 2 & 3')
    if div_2_ == 0 and div_3_ != 0:
        print('Divisible only by 2 not by 3')
    if div_2_ != 0 and div_3_ == 0:
        print('Divisible only by 3 not by 2')
    if div_2_ != 0 and div_3_ != 0:
        print('Not divisible by both 3 & 2')
    
    os._exit

else:
    print('enter a number greater then 3')
    os._exit


