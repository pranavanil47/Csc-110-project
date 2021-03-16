###
### Author: ?
### Course: ?
### Description: ?
###

from graphics import graphics

# Some constants to be used throughout the code
# The literals 'X' and 'O' and ' ' should not be used elsewhere
WHITE = 'O'
BLACK = 'X'
EMPTY = ' '

def is_move_acceptable(board, turn, pos):
    if pos in range(1,12) and board[pos] == '':
        return True
    else:
        return False
    ''' Implement '''
    pass

def move(board, turn, pos):
    ''' Implement '''
    pass

def get_move(turn):
    ''' Implement '''
    pass

def is_over(board):
    ''' Implement '''
    pass

def get_opposite_turn(turn):
    ''' Implement '''
    pass

def print_board(board):
    ''' Implement '''
    
    print('+-----------------------+')
    print('|'+board[0]+ '|'+board[1]+ '|'+board[2]+ '|'+board[3]+ '|'+board[4]+ \
        '|'+board[5]+ '|'+board[6]+ '|'+board[7]+ '|'+board[8]+ '|'+board[9]+ \
            '|'+board[10]+ '|'+board[11]+ '|')
    print('+-----------------------+')
    pass

def draw_board(board, gui):
    ''' Implement '''
    pass

def who_is_winner(board):
    ''' Implement '''
    pass

def main():
    print('WELCOME TO REVERSI')

    gui = graphics(700, 200, 'reversi')

    # Initialize an empty list with 12 slots
    board = [EMPTY] * 12
    # State of whether or not the game is over
    over = False
    # Starting turn (should alternate as gome goes on)
    turn = BLACK

    # Print out the initial board
    print_board(board)
    draw_board(board, gui)

    # Repeatedly process turns until the game should end (every slot filled)
    while not over:
        place_to_move = get_move(turn)
        while not is_move_acceptable(board, turn, place_to_move):
            place_to_move = get_move(turn)
        move(board, turn, place_to_move)

        print_board(board)
        draw_board(board, gui)

        over = is_over(board)
        turn = get_opposite_turn(turn)
    print('GAME OVER')
    print(who_is_winner(board))

main()
