counts = {}

words_file = open('words1.txt', 'r')
for line in words_file:
    word  = line.strip('\n')
    if word not in counts:
        counts[word]=0
    counts[word]+=1

for key,value in counts.items():
    print(key, value)
