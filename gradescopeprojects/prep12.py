def average_numbers(num):
    count = 0
    i =  0 
    while num > i:
        integer = int(input('Number:\n'))
        count += integer
        i+= 1
    avg_value_ = count/num
    print('Average =',round(avg_value_, 2))
    