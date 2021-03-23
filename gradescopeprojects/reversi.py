
from graphics import graphics

# Some constants to be used throughout the code
# The literals 'X' and 'O' and ' ' should not be used elsewhere
WHITE = 'O'
BLACK = 'X'
EMPTY = ' '

def is_move_acceptable(board, turn, pos):
    """
    Checks if the board is empty or full

    :param board: The board is a list
    :param turn:  checks whether it is white or black's turn
    :param pos: position of the element on the board
    :return: True or False
    """
    if board[pos - 1] == EMPTY and pos in range(1,14):
        return True
    return False

def move(board, turn, pos):
    """
    Checks the location of the constants and assigns nee pieces

    :param board: The board is a list
    :param turn:  checks whether it is white or black's turn
    :param pos: position of the element on the board
    :return: True or False
    """
    position = pos - 1
    board[position] = turn
    player = get_opposite_turn(turn)
    i = position + 1
    while i < len(board) and board[i] == player:
        i += 1
    if i < len(board) and board[i] == turn:
        for x in range(position+1,i,1):
            board[position] = turn
    i = position - 1

    while i > -1 and board[i] == player:
        i -= 1

    if i > -1 and board[i] == turn:
        for y in range(i+1,position,1):
            board[y] = turn

def get_move(turn):
    """
    Asks the user to input the position of the piece

    :param board: The board is a list
    :param turn:  checks whether it is white or black's turn
    :param pos: position of the element on the board
    :return: position of the piece
    """
    if turn == WHITE:
        value = input("O Enter a value: ")
    if turn == BLACK:
        value = input("X Enter a value: ")
    return int(value)

def is_over(board):
    """
    Determines when the reversi game is over

    :param board: The board is a list
    :param turn:  checks whether it is white or black's turn
    :param pos: position of the element on the board
    :return: True or False
    """

    not_full = False
    i = 0
    while i < len(board):
        if i == EMPTY:
            not_full = True
        else:
            not_full = False
        i += 1
    return not_full


def get_opposite_turn(turn):
    """
    Switches the white pieces to black and the black pieces to white

    :param turn:  checks whether it is white or black's turn
    :return: True or False
    """

    if turn == WHITE:
        return BLACK
    if turn == BLACK:
        return WHITE

def print_board(board):
    """
    Switches the white pieces to black and the black pieces to white

    :param board: The board is a list
    :return: None
    """

    print("+-----------------------+")
    for x in range(len(board)):
        print("|" + board[x], end="")
    print("|")
    print("+-----------------------+")

def draw_board(board, gui):
    """
    Displays the GUI version of the reversi game

    :param board: The board is a list
    :param gui: Graphical User Interface
    :return: None
    """


    gui.clear()
    gui.text(250,20,"REVERSI","black",40)
    for index in range(50,650,50):
        gui.rectangle(index,100,50,50,"green")
        gui.line(index,100,index,150,"blue",3)
    gui.line(650, 100, 650, 150, "blue",3)
    gui.line(50, 100, 650, 100, "blue", 3)
    gui.line(50, 150, 650, 150, "blue", 3)
    marker1_x = 65
    marker2_x = 60
    for i in range(len(board)):
        if board[i] == WHITE:
            gui.text(marker2_x,100,"O","black",30)
        elif board[i] == BLACK:
            gui.text(marker1_x,100,"X","black",30)
        marker1_x += 50
        marker2_x += 50

    gui.update_frame(30)

def who_is_winner(board):
    count_white = 0
    count_black = 0
    for x in board:
        if x == "X":
            count_black += 1
        else:
            count_white += 1
    if count_white > count_black:
        print("WHITE WINS")
    elif count_black > count_white:
        print("BLACK WINS")
    else:
        print("THERE IS A TIE")


def main():
    """
    In charge of running the other functions

    :return: None
    """
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