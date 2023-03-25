from random import randrange 

# this is made with the specifications from a lab in the Python Foundation's Python 
# Essentials course, which should explain some quirks in the logic

board = [[1,2,3],[4,"X",6],[7,8,9]]

def display_board(board):
    print("+-------+-------+-------+\n"+\
          "|       |       |       |\n"+\
          "|  ",board[0][0],"  |  ",board[0][1],"  |  ",board[0][2],"  |\n"+\
          "|       |       |       |\n"+\
          "+-------+-------+-------+\n"+\
          "|       |       |       |\n"+\
          "|  ",board[1][0],"  |  ",board[1][1],"  |  ",board[1][2],"  |\n"+\
          "|       |       |       |\n"+\
          "+-------+-------+-------+\n"+\
          "|       |       |       |\n"+\
          "|  ",board[2][0],"  |  ",board[2][1],"  |  ",board[2][2],"  |\n"+\
          "|       |       |       |\n"+\
          "+-------+-------+-------+\n"\
          )

def move_translator(move):
    for i in board: 
        if move in i:
            return board.index(i), i.index(move)

def enter_move(board):
    move = 0
    while not move > 0 and move < 10:
        move = int(input("Make your move: "))
        board_move = move_translator(move)
        if board_move == None:
            continue
        else:
            board[board_move[0]][board_move[1]] = "O"


def make_list_of_free_fields(board):
    global free
    free = []
    for i in board:
        for p in i:
            if type(p) is int:
                free.append((board.index(i), i.index(p)))

def draw_move(board):
    initial_move = randrange(1, 10)
    board_move = move_translator(initial_move)
    while not board_move in free:
        initial_move = randrange(1, 10)
        board_move = move_translator(initial_move)
    board[board_move[0]][board_move[1]] = "X"


def victory_for(board, sign):
    line = ""
    column = ""
    diagonal = ""
    for i in board:
        for p in i:
            line += str(p)
        if line == sign*3:
            return True
        else:
            line = ""
    for i in range(len(board)):
        for p in range(len(board)):
            column += str(board[p][i])
        if column == sign*3:
            return True
        else:
            column = ""
    for i in range(len(board)):
        diagonal += str(board[i][i])
    if diagonal == sign*3:
            return True
    else:
        diagonal = ""
        for i in range(len(board)):
            diagonal += str(board[i][-i-1])
    if diagonal == sign*3:
            return True

def draw(board):
    for i in board:
        for p in i:
            if not type(p) is str:
                return
    return True


while not (victory_for(board, "X") or victory_for(board, "O") or draw(board)):
    display_board(board)
    enter_move(board)
    if victory_for(board, "O"):
        break
    make_list_of_free_fields(board)
    draw_move(board)

display_board(board)

if victory_for(board, "X"):
    print("Computer wins")
elif victory_for(board, "O"):
    print("You win")
else:
    print("Draw")