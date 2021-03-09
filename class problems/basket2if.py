w = int(input('enter court width\n'))
s1 =input('Enter first team score:\n')
s2 =  input('Enter second team score:\n')
print (' ')

if w % 2 == 0:
   # s1 = s1.ljust(3)
    #s2 = s2.ljust(3)

    print('+-------------+')
    print('|    SCORE    |')
    print('|  ', s1 ,' '+ s2 +'  |')
    print('+-------------+')

    hf = w//2

    print('+--------'+ '-' * hf + '----' + '-' * hf + '--------+')
    print('|        '+ ' '* hf+'    '+ ' ' * hf +'        |')
    print('|-----++ ' + ' ' * hf + '    ' + ' ' * hf + ' ++-----|')
    print('|O | |   '+ ' ' * hf + 'SUNS'+ ' ' * hf+ '     | O|')
    print('|-----++ ' + ' ' * hf + '    ' + ' ' * hf + ' ++-----|')
    print('|        '+ ' '* hf+'    '+ ' ' * hf +'        |')
    print('+--------'+ '-' * hf + '----' + '-' * hf + '--------+')
    
else :
    hf = w//2

    print('+--------'+ '-' * hf + '----' + '-' * hf + '--------+')
    print('|        '+ ' '* hf+'    '+ ' ' * hf +'        |')
    print('|-----++ ' + ' ' * hf + '    ' + ' ' * hf + ' ++-----|')
    print('|O | |   '+ ' ' * hf + 'SUNS'+ ' ' * hf+ '     | O|')
    print('|-----++ ' + ' ' * hf + '    ' + ' ' * hf + ' ++-----|')
    print('|        '+ ' '* hf+'    '+ ' ' * hf +'        |')
    print('+--------'+ '-' * hf + '----' + '-' * hf + '--------+')
