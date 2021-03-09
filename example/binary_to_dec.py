



binary_string_ = input('Enter binary\n')


decimal_count_ = 0
i = len(binary_string_) - 1 

power = 0

while i >= 0:
    if binary_string_[i]== '1':
        decimal_count_ += 2 ** power
    
    power +=1
    i -= 1

print(decimal_count_)

    ### 10010100 = 148
    