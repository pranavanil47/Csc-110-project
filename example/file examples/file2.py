info = open('file1_text.txt', 'r')
line = info.readline()
lines = info.readlines()
for i in lines:
    print(i)
line = info.readline()
print(line)