'''
swap sam with rome
there are two meathods
'''
names = ['joe', 'sam', 'alex', 'rome', 'alice']
'''
temp = names[1]

names[1] = names[3]
names[3] = temp
'''

names[1], names[3] = names[3], names[1]

print(names)