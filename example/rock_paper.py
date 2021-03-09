import random

def computer_rps():
    choice = random.randint(0,2)
    if choice == 0:
        return 'rock'
    elif choice == 1:
        return 'paper'
    else:
        return 'scissors'

def user_rps():
    choice_user = input('Enter rock, paper or scissors:   ')
    while choice_user != 'rock' and choice_user != 'scissors' \
        and choice_user != 'paper':
       choice_user = input('Enter rock, paper or scissors:   ')
    return choice_user

def win_fxn(user, comp):
    if user == 'rock' and comp == 'scissors':
        print('computer chose scissors')
        print('You win')
        print('ggwp')
    elif user == 'rock' and comp == 'paper':
        print('computer chose paper')
        print('You loose')
        print('lol')
    elif user == 'paper' and comp == 'scissors':
        print('computer chose scissors')
        print('You loose')
        print('lol')
    elif user == 'paper' and comp == 'rock':
        print('computer chose rock')
        print('You win')
        print('ggwp')
    elif user == 'scissors' and comp == 'paper':
        print('computer chose paper')
        print('You win')
        print('ggwp')      
    elif user == 'scissors' and comp == 'rock':
        print('computer chose rock')
        print('You loose')
        print('lol')
    else:
        print('both chose', user)
        print('its a draw!!!')
    pass

def main():
    comp_selection = computer_rps()
    user_selection = user_rps()
    win_fxn(user_selection, comp_selection)

main()