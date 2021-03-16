info = open('numbers.txt', 'r')
lines = info.readlines()

for line in lines:
    s = line.split(',')
    if int(s[1])>15:
        to_print = s[2].strip('\n')
        print(to_print)