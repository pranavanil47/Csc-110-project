###
### Author: Pranav I Anilkumar   
###  Class: CSc 110
### Description: A program that prints out a AT-AT with three inputs from the user
###              ; the neck length, the body height, and the leg height. 
###

neck_length = int(input('Neck Length:\n'))
body_height = int(input('Body Height:\n'))
leg_height = int(input('Leg Height:\n'))
print(' ')



print('     _,.-Y  |  |  Y-._       ')     
print(' .-~"   ||  |  |  |   "-. ')
print(' |______________________|\n' * body_height,end='')  
print(' |______________________|    ' + ' ' * neck_length +'_____')
print(' L______________________[---' + '-' * neck_length +'I\" .-{\"-.')
print('I____________________ [__L]' + '_' * neck_length +'[I_/r(=}=-P')
print('L________________________j~ ' + ' '* neck_length +'\'-=c_]/=-^')
print('\________________________]')
print('  [___________________]')
print('     I--I\"~~\"\"\"~~\"I--I')
print('     |\\n|         |\\n|\n' * leg_height ,end='')
print('     ([])         ([])')
print('    /|..|\       /|..|\\')
print('   |=}--{=|     |=}--{=|')
print('  .-^--e-^-.   .-^--e-^-.')