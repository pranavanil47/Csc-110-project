word_count ={'beluga':1,'Bar':15, 'Bend':3,'Behave':8}

words = ['end', 'have', 'bar']

for word in words:
    if word in word_count:
        print(word, 'has a count')