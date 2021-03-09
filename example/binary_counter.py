binary = input('Enter binary\n')

count_1_ = 0
count_0_ = 0
i = 0
while i <= len(binary) - 1:
    if binary[i] == '1':
        count_1_ += 1
    elif binary[i] == '0':
        count_0_ += 1
    
    else :
        print('yo enter a binary bitch')

    i += 1
    

print('the no of 1\'s', count_1_)
print('the no of 0\'s', count_0_)   
 