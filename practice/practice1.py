f1 = open('one.txt', 'w')
f1.write('steak\nchicken\nham')
f1.close()

f2 = open('one.txt', 'r')
f3 = open('one.txt', 'a')

for line in f2:
    f3.write((line))
f2.close()
f3.close()