names= ['a','b', 'c','d', 'e', 'f']
x =len(names)-1
i =0
for i in range(0, len(names)//2):
    names[i], names[(x-i)] = names[x-i],names[i]
    

print(names)