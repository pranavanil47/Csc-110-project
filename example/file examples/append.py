words = open('append.txt', 'a')
words.write('the slow bear\n')
words.write(' jumped over the bear\n')
words.close()

words = open('test1.txt', 'r')
print(words.readline())