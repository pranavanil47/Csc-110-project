names = {'jonas', 'james','zac'}

for element in names:
    print(element)

word = {'army':'ymra'}
line = 'Z S Y M R A Z'
line =  line.lower()
line_list = line.split(' ')
print(line_list)
line_to_check = ''.join(line_list)
print(line_to_check)
for key, value in word.items():
    
    if key or value in line_to_check:
        print(True)
    else:
        print(False)

title = 'willie'
name = title
print(name+ ' ' + title)
title = 'josh'
print(name+ ' '+ title)
name_b = name
name = 'stanley'
print(name+' '+ name_b+ ' '+ title)

