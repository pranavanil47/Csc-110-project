###
### Author: Pranav I Anilkumar  
### Class: CSc 110
### Description: A program that can print out three pre-designed avatars and also a custom 
###              avatar according to the user inputs.
###

def hat(string_input):
    '''
    This function prints out the types of hat 
    right, left, both and front.
    '''
    if string_input == 'left':
        print('       ~-~ ')      
        print('     /-~-~-\\')    
        print(' ___/_______\\')
    elif string_input == 'right':
        print('       ~-~  ')     
        print('     /-~-~-\\')     
        print('    /_______\___')
    elif string_input == 'both':
        print('       ~-~ ')      
        print('     /-~-~-\\')     
        print (' ___/_______\___')
    elif string_input == 'front':
        print ( '       ~-~' )      
        print('     /-~-~-\\')     
        print('    /_______\\' )
     

def face(hair, eyes):
    '''
    This function prints out the face with two 
    parameters; the eye characher and whether the
    avatar needs long hair or not
    '''
    if hair == 'True':
        print('   \"|"""""""|\"')   
        print('   \"| '+ eyes +'   '+ eyes +' |\"')   
        print('   \"|   V   |\"')    
        print('   \"|  ~~~  |\"')    
        print('   \" \_____/ \"')
    elif hair == 'False':
        print('    |\'\'\'\'\'\'\'|')   
        print('    | '+ eyes +'   '+ eyes +' |')   
        print('    |   V   |')    
        print('    |  ~~~  |')    
        print('     \_____/ ')

def arms(charchter_string):
    '''
    This function prints out the arms of the
    avatar with the desired charachter as arms.
    '''
    print(' 0'+ charchter_string * 4 + '|---|'+ charchter_string * 4+'0')

def torso(length):
    '''
    This function prints out the torso according 
    to the desired length.
    '''
    i = 0
    while i < int(length):     ### Creating a while loop that prints out the
        print('      |-X-|')   ## torso until the length requirement is met.
        i +=1      

def legs(leg_length, shoes):
    '''
    This function prints out the legs and shoes according to 
    the two parameters; leg length and the shoe charachters.
    '''
    print('      HHHHH')
    i = 0
    between_space = 1                                                      ##space between the legs
    start_space = 4                                                      ##space before the start of the print
    while i < int(leg_length):                                             ### Creating a while loop that prints out the leg according to the
        print(' ' * start_space +' ///'+ ' ' * between_space +'\\\\\ ')    ## leg length provided 
        i += 1
        between_space += 2 
        start_space -= 1
    
    print(shoes+ ' ' * 7 + shoes)   ### This prints out the shoes 

def jeff_print():
    '''
    This function prints out the pre-designed Jeff Avatar
    when called. The aruguments are given beforehand. 
    ''' 
    hat('both')
    face('False', '0')
    print('      |-X-|')
    arms('=')
    torso(4)
    legs(2,'#HHH#')

def jane_print():
    '''
    This function prints out the pre-designed Jane Avatar
    when called.The aruguments are given beforehand.  
    ''' 
    hat('right')
    face('True', '*')
    arms('T')
    torso(2)
    legs(3,'<|||>')

def chris_print():
    '''
    This function prints out the pre-designed Chris Avatar
    when called. The aruguments are given beforehand. 
    ''' 
    hat('front')
    face('False', 'U')
    print('      |-X-|')
    arms('W')
    torso(2)
    legs(4, '<>-<>')

def custom():
    '''
    This function takes inputs from the user and uses them as 
    arguments at the respective functions to create a custom
    avatar.
    '''
   
    hat_input = input('Hat style ?\n')
    eyes_input = input('Character for eyes ?\n')
    hair_input = input('Long hair (True/False) ?\n')
    arms_input = input('Arm style ?\n')
    torso_input = int(input('Torso length ?\n'))
    legs_input = int(input('Leg length (1-4) ?\n'))
    shoes_input = input('Shoe look ?\n')
    print()

    hat(hat_input)                       
    face(hair_input, eyes_input)
    arms(arms_input)
    torso(torso_input)
    legs(legs_input, shoes_input)

def exit():
    '''
    This function is called just to print
    out an empty line and exit
    '''
    print()

def main():
    '''
    This is main fuction where the type of avatar is taken from the user and 
    printed out. the types are Jeff, Jane, Chris, exit and custom.
    '''
    print('----- AVATAR -----')
    avatar_type = input('Select an Avatar or create your own:\n') 
    while avatar_type != 'exit' and avatar_type != 'custom' and \
        avatar_type != 'Jeff' and avatar_type != 'Jane' and avatar_type != 'Chris':
        avatar_type = input('Select an Avatar or create your own:\n')
    if avatar_type == 'exit':   
        exit()
    elif avatar_type == 'Jeff':
        print()
        jeff_print()
    elif avatar_type == 'Jane':
        print()
        jane_print()
    elif avatar_type == 'Chris':
        print()
        chris_print()
    elif avatar_type == 'custom': 
        print('Answer the following questions to create a custom avatar')
        custom()
 

main()
