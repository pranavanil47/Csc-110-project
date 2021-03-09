value = ['jan', 65, 'jon', 78, 'kai', 40] 

i =1
while i <len(value):
    if value[i]<52 or value[i]>76:
        value.pop(i)
        value.pop(i-1)
    else:
        i +=2

print(value)
