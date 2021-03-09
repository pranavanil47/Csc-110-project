
user_input = input('enter some names;  ')
name = user_input.split(' ')

total = 0
for e in name:
    total += len(e)

print('avg name length =', (total/len(name)))