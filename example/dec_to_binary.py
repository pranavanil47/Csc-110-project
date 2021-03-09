

num = int(input('Enter number less than 1024 to convert to binary\n'))

binary_string = ''
power = 10

while power >= 0:
    calc = 2 ** power
    if calc <= num:
        num = num - calc
        binary_string += '1' 
    
    else:
        binary_string+= '0'
    
    power -=1 


print(binary_string)

#10010100 = 148