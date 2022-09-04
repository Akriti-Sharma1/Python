'''
 X | O | X
---+---+---
 O | O | X
---+---+---
   | X |
'''

import random


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3)
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")



def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

def take_integer(square_num):
    coord = [0,0]
    if 1 <= square_num <= 3:
        coord[0] = 0
        coord[1] = square_num-1
    elif 4 <= square_num <= 6:
        if 4 <= square_num <= 5:
            coord[0] = 1
            coord[1] = (square_num-2) // 3
        elif square_num == 6:
            coord[0] = 1
            coord[1] = 2
    elif 7 <= square_num <= 9:
        if 7 <= square_num <= 8:
            coord[0] = 2
            coord[1] = (square_num-5) // 3
        elif square_num == 9:
            coord[0] = 2
            coord[1] = 2
    else:
        return "Invalid Input"

    return coord

def put_in_board(board, mark, square_num):
    coord = take_integer(square_num)
    board[coord[0]][coord[1]] = mark

# Write a loop that asks for the user to alternately enter coordinates for "X"s and "O"s such that two users can play against each other as shown in the example above.
# Here is a piece of code that counts how many times the user failed to input "hi" when repeatedly trying.
def play_game():
    count = 0
    checker = []
    square_num = 0
    print("Player One, you are X. Player Two, you are O.")
    while(count < 9):
        if count % 2 == 0:
            square_num = input("Enter your move: ")
            square_num = int(square_num)

            if square_num in checker:
                print("This square is already taken.")
            else:
                checker.append(square_num)
                put_in_board(board, "X", square_num)
                print_board_and_legend(board)
                count += 1
            if is_win(board, "X") or is_win(board, "O"):
                break
        else:
            square_num = input("Enter your move: ")
            square_num = int(square_num)

            if square_num in checker:
                print("This square is already taken.")
            else:
                checker.append(square_num)
                put_in_board(board, "O", square_num)
                print_board_and_legend(board)
                count += 1
            if is_win(board, "X") or is_win(board, "O"):
                break
    print("Done!")

# Write a function with the signature get_free_squares(board) which creates and returns a new list which
# contains a list of the coordinates of the free squares in the board. For example, if the board is represented
# as follows
def get_free_squares(board):
    new = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == ' ':
                new.append([i,j])
    return new

# Now write a function make_random_move(board, mark) that finds a random free square in board, and
# puts the string mark in the free square. Hint: you can print a random number between 0 and n-1 as
# follows:
# import random
# print(n * random.random())

def make_random_move(board,mark):
    #new = get_free_squares(board)
    checker = False
    while(checker != True):
        random_i = int(3 * random.random())
        random_j = int(3 * random.random())
        if board[random_i][random_j] == ' ':
            board[random_i][random_j] = mark
            checker = True
        else:
            checker = False
    return board


def play_game_comp():
    count = 0
    checker = []
    square_num = 0
    print("Player One, you are X. Player Two is the computer.")
    while(count < 8 or is_win(board,"X") == False or is_win("O") == False):
        if count % 2 == 0:
            square_num = input("Enter your move: ")
            square_num = int(square_num)
            get_free_squares(board)

            if take_integer(square_num) in get_free_squares(board):
                put_in_board(board, "X", square_num)
                print_board_and_legend(board)
                count += 1
            else:
                print("This square is already taken.")
        else:
            #make_random_move(board, "O")
            improve_comp(board)
            print_board_and_legend(board)
            count += 1
        if is_win(board, "X") or is_win(board, "O"):
            break

    print("Done!")

# Write a function with the signature is_row_all_marks(board, row_i, mark) which returns True iff the row with index row_i in board contains 3 marks equal to mark.
def is_row_all_marks(board, row_i, mark):
    checker = 0
    for i in range(len(board)):
        if board[row_i][i] == mark:
            checker += 1
        else:
            checker = 0
    if checker == 3:
        return True
    else:
        return False

# Write a function with the signature is_col_all_marks(board, col_i, mark) which returns True iff the column with index row_i in board contains 3 marks equal to mark.
def is_col_all_marks(board, col_i, mark):
    checker = 0
    for i in range(len(board)):
        if board[i][col_i] == mark:
            checker += 1
        else:
            checker = 0
    if checker == 3:
        return True
    else:
        return False

def is_diag_all_marks(board, mark):
    checker = 0
    for i in range(len(board)):
        if board[i][i] == mark:
            checker += 1
        else:
            for j in range(len(board), -1):
                if board[i][j] == mark:
                    print(j)
                    checker += 1
    if checker == 3:
        return True
    else:
        return False
# Using the functions above, and also checking the diagonals, write a function with the signature is_win(board, mark) that returns True iff the mark mark won on the board board (i.e., there is a line of 3 marks somewhere in board).
def is_win(board,mark):
    for i in range(len(board)):
        if is_row_all_marks(board, i, mark) == True or is_col_all_marks(board, i, mark) == True or is_diag_all_marks(board, mark) == True:
            won = True
        else:
            return False
    if won == True:
        return True

def improve_comp(board):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ' ':
                    board[i][j] = "O"
                    return board
                    if is_win(board, "O") == False:
                        board[i][j] = ' '
        make_random_move(board, "O")



if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)

    print("\n\n")
    #print(take_integer(1))
    #board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
#     put_in_board(board, "O", 4)
#     put_in_board(board, "O", 5)
#     put_in_board(board, "O", 6)
#     print(is_row_all_marks(board, 1, "O"))
    play_game_comp()