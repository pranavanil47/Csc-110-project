ages = [35,35,23,18,45,19,72]
'''
try:
    print(ages[0]+ ages[4])

except:
    print('Failure')

try:
    for i in range(len(ages)):
        if ages[i] > ages[i+1]:
            print(ages[i])

except:
    print('failed')

print(' ')
'''

for i in range(len(ages)):
    try:
        if ages[i]> ages[i+i]:
            print(ages[i])
    except:
        print('failed')
print(ages[-1])

