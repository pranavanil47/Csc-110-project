###
### Author : Pranav I Anilkumar
### Class : CSc 110
### Description : A program that prints out a nebulon with the inputs from the user on the
###               the lengt and the number of layers.    
###

large_bottom = int(input('Large Layers on bottom:\n'))                                                       #lb - large_bottom 
medium_bottom = int(input('Medium Layers on bottom:\n'))                                                              #mb - medium_bottom
small_bottom = int(input('Small Layers on bottom:\n'))                                                               #sb - small_bottom 
front_length  = int(input('Front length:\n'))                                                                         #fl - front_length  
middle_length = int(input('Middle length:\n'))                                                                        #ml - middle_length
back_length = int(input('Back length:\n'))                                                                          #bl - back_length
print(' ')

print('  /=' + '-'* front_length +'\         ' +' '* middle_length+'/' + '-' * back_length + '|')
print(' /==' +'/' * front_length  + '==\\\\\    '+ ' ' * middle_length +\
    '|' + '=' * back_length+ '=|')
print('|==-'+'\\' * front_length  +'======\\--=='+'=' * middle_length + \
    '=' * back_length + '|')
print(' \\'+'=' * front_length  +'====' + '---------' + '-' * middle_length \
    + '-' * back_length + '|')
print('  \\='+ '-' * front_length  + '=///     ' + ' ' * middle_length + '\\'+ \
    '=' * back_length +'=/')
print (('   /'+'-' * (front_length -3)+'|\n'+ '   \\' +'=' *(front_length -3)+'|\n') * large_bottom,end='')
print((' ' * (front_length -(front_length //2)) +'/' + '+' * (front_length //2) \
    +'|\n' + ' ' * (front_length -(front_length //2))  + '\\'+ '-' * (front_length //2) + '|\n') * medium_bottom,end='')   
print(( ' ' *  ((front_length -(front_length //3))-1) +'\\' +'<' *(front_length //3) \
    +'|\n' +' ' *((front_length -(front_length //3))) + '<'*(front_length //3)+'|\n') * small_bottom,end='')
      