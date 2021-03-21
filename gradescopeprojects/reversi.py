###
### Author: ?
### Course: ?
### Description: ?
###

from graphics import graphics

# Some constants to be used throughout the code
# The literals 'X' and 'O' and ' ' should not be used elsewhere

def is_move_acceptable(board, turn, pos):
    pos = pos - 1 
    WHITE = 'O'
    BLACK = 'X'
    EMPTY = ' '

    if pos in range(0,12) and board[pos] == EMPTY:
        return True
    else:
        return False
    ''' Implement '''
    pass

def move(board, turn, pos):
    WHITE = 'O'
    BLACK = 'X'
    EMPTY = ' '
    pos = pos - 1

    if turn == BLACK:
        board[pos] = BLACK
        if  board[pos-1]!= EMPTY:
            i = pos-2
            while board[i] == BLACK:
                board[i] = BLACK
                i-=1
                    

              
    
    elif turn == WHITE:
        board[pos] = WHITE
        if board[pos-1]!= EMPTY:
            i = pos-2
            while board[i] == WHITE:
                board[i] = WHITE
                i-=1
                    
    ''' Implement '''

def get_move(turn):
    ''' Implement '''
    WHITE = 'O'
    BLACK = 'X'
    EMPTY = ' '
    if turn == BLACK:
        value = int(input('X choose your move:\n'))
    elif turn == WHITE:
        value = int(input('O choose your move:\n'))

    
    return value
   

def is_over(board):
    ''' Implement '''
    WHITE = 'O'
    BLACK = 'X'
    EMPTY = ' '

    for i in range(len(board)):
        if board[i] == EMPTY:
            return False
    return True    
    pass

def get_opposite_turn(turn):
    WHITE = 'O'
    BLACK = 'X'
    EMPTY = ' '

    if turn == WHITE:
        return BLACK
    elif turn == BLACK:
        return WHITE

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
'''
def draw_board(board, gui):
    
    pass
'''
def who_is_winner(board):
    ''' Implement '''
    black_count = 0
    white_count = 0
    for i in range(len(board)):
        if board[i] == 'X':
            black_count +=1
        elif board[i] == 'O':
            white_count +=1
    
    if white_count > black_count:
        print('white wins')
    else:
        print('black wins')
    pass

def main():
    print('WELCOME TO REVERSI')
    WHITE = 'O'
    BLACK = 'X'
    EMPTY = ' '


    #gui = graphics(700, 200, 'reversi')

    # Initialize an empty list with 12 slots
    board = [EMPTY] * 12
    # State of whether or not the game is over
    over = False
    # Starting turn (should alternate as gome goes on)
    turn = BLACK

    # Print out the initial board
    '''
    print_board(board)
    draw_board(board, gui)
    '''

    # Repeatedly process turns until the game should end (every slot filled)
    while not over:
        place_to_move = get_move(turn)
        while not is_move_acceptable(board, turn, place_to_move):
            place_to_move = get_move(turn)
        move(board, turn, place_to_move)

        print_board(board)
        '''
        draw_board(board, gui)
        '''

        over = is_over(board)
        turn = get_opposite_turn(turn)
    print('GAME OVER')
    print(who_is_winner(board))

main()
