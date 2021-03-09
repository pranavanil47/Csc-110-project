def print_num(first,second, third):
    if first >= second >= third or second >= first >= third:
        print(first + second)
    elif first >= third >= second or third >= first >= second:
        print(first + third)
    else: 
        print(second + third)

print_num(30, 10, 20)
print_num(10, 20, 30)
print_num(20, 30, 10)
