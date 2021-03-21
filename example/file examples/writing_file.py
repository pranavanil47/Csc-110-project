a_file = open('a.txt','w')
a_file.write('Hi there')
a_file.close()

b_file = open('a.txt')
print(b_file.readline())