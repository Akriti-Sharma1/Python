def is_empty(board):
    for i in range(len(board)-1):
        for j in range(len(board)-1):
            if board[i][j] != " ":
                return False

    return True


def is_bounded(board, y_end, x_end, length, d_y, d_x):
    s = board[y_end][x_end]
    new_y_end = y_end
    new_x_end = x_end
    y_end_checker = y_end
    x_end_checker = x_end
    if s == " ":
        right = False
        left = False
    else:
        right = True
        left = True
    x_end_left = x_end
    y_end_left = y_end
    x_end_right = x_end
    y_end_right = y_end
    d_y = d_y * -1
    d_x = d_x * -1
    i = 0
#     right = True
#     left = True
    #print(right, left)
    while 0 <= y_end <= 7 and 0 <= x_end <= 7 and board[y_end][x_end] == s:
        i += 1
        y_end += d_y
        x_end += d_x

    while 0 <= y_end_checker <= 7 and 0 <= x_end_checker <= 7 and board[y_end_checker][x_end_checker] == s:
        i += 1
        y_end_checker -= d_y
        x_end_checker -= d_x

#     for _ in range(length):
#         if board[y_end][x_end] == s:
#             i += 1
#         y_end += d_y
#         x_end += d_x
#     print(s)
    #print(i)
    #new_y_end = y_end
    #new_x_end = x_end
#     d_y = d_y * -1
#     d_x = d_x * -1
    if i-1 == length:
#         print(new_x_end)
#         print(d_x)
        d_y = d_y*-1
        d_x = d_x * -1
        if 0 <= new_y_end+d_y <= 7 and 0 <= (new_x_end+d_x) <= 7:
            #print(y_end+d_y)
            #print(new_x_end+d_x)
            if board[new_y_end+d_y][new_x_end+d_x] != " ":
            #if board[new_y_end+d_y][new_x_end+d_x] != " ":
                right = False
            elif board[new_y_end+d_y][new_x_end+d_x] == s:
                right = False
#             else:
#                 right = False
        else:
            right = False

        # print(new_x_end+(d_x*length))
        d_y = d_y*-1
        d_x = d_x * -1
        if 0 <= new_y_end+(d_y*length) <= 7 and 0 <= new_x_end+(d_x*length) <= 7:
            # print(new_x_end+(d_x*length))
#             print(new_y_end+(d_y*length))
            if board[new_y_end+(d_y*length)][new_x_end+(d_x*length)] != " ":
            #if board[new_y_end+(d_y*length)][new_x_end+(d_x*length)] != " ":
                left = False
            elif board[new_y_end+(d_y*length)][new_x_end+(d_x*length)] == s:
                left = False
#             else:
#                 left = False
        else:
            #print("hello")
            left = False
    else:
        right = False
        left = False

    #print(right, left)
    if right == True and left == True:
        return "OPEN"
    elif right == True and left == False:
        return "SEMI OPEN"
    elif right == False and left == True:
        return "SEMI OPEN"
    elif right == False and left == False:
        return "CLOSED"


def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_seq_count = 0
    semi_open_seq_count = 0
    #i = 0
#     x_end = x_start
#     y_end = y_start
    while 0 <= y_start <= 7 and 0 <= x_start <= 7:
        for i in range(7):
            #print(y_start, x_start)
            while 0 <= y_start <= 7 and 0 <= x_start <= 7:
                #print(y_start, x_start)
                i = 0
                if board[y_start][x_start] == col:
                    while 0 <= y_start <= 7 and 0 <= x_start <= 7 and board[y_start][x_start] == col:
                        #print(y_start, x_start)
                        i += 1
                        y_start += d_y
                        x_start += d_x
                        #print(i)
                    if i == length:
                        y_start -= d_y
                        x_start -= d_x
                        #print(y_start,x_start)
                        # print(is_bounded(board, y_start, x_start, length, d_y, d_x))
                        if is_bounded(board, y_start, x_start, length, d_y, d_x) == "OPEN":
                            open_seq_count += 1
                        elif is_bounded(board, y_start, x_start, length, d_y, d_x) == "SEMI OPEN":
                            semi_open_seq_count += 1
                else:
                    y_start += d_y
                    x_start += d_x
            else:
                y_start += d_y
                x_start += d_x

                #print(i)
    return open_seq_count, semi_open_seq_count

def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0
    for i in range(0, len(board)):
        tuple_horizontal = detect_row(board, col, 0, i, length, 0, 1)
        tuple_vertical = detect_row(board, col, 0, i, length, 1, 0)
        tuple_upper_left = detect_row(board, col, 0, i, length, 1, 1)
        tuple_upper_right = detect_row(board, col, 0, i, length, 1, -1)
#         print(tuple_horizontal)
#         print(tuple_vertical)
#         print(tuple_upper_left)
#         print(tuple_upper_right)
#         print(0,i)
#         print("\n")
        open_seq_count += (tuple_horizontal[0]+tuple_vertical[0]+tuple_upper_left[0] + tuple_upper_right[0])
        semi_open_seq_count += (tuple_horizontal[1]+tuple_vertical[1]+tuple_upper_left[1] + tuple_upper_right[1])

    for i in range(1, len(board)):
        tuple_horizontal = detect_row(board, col, i, 0, length, 0, 1)
        tuple_upper_left = detect_row(board, col, i, 0, length, 1, 1)
        tuple_upper_right = detect_row(board, col, i, 0, length, 1, -1)
        open_seq_count += (tuple_horizontal[0]+tuple_vertical[0]+tuple_upper_left[0] + tuple_upper_right[0])
        semi_open_seq_count += (tuple_horizontal[1]+tuple_vertical[1]+tuple_upper_left[1] + tuple_upper_right[1])
    return open_seq_count, semi_open_seq_count

    ####CHANGE ME



def search_max(board):
    check_score = -10000000
    move_y = 0
    move_x = 0
    if is_win == "Black won" or is_win == "White won":
        return is_win(board)
    else:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == " ":
                    #print(i,j)
                    board[i][j] = "b"
                    if score(board) > check_score:
                        check_score = score(board)
                        move_y = i
                        move_x = j
                    board[i][j] = " "
    return move_y, move_x

def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)


    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4])+
            500  * open_b[4]                     +
            50   * semi_open_b[4]                +
            -100  * open_w[3]                    +
            -30   * semi_open_w[3]               +
            50   * open_b[3]                     +
            10   * semi_open_b[3]                +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

def is_row_all_marks(board, mark):
    checker = 0
    for i in range(len(board)):
        for j in range(len(board)):
            #print(board[i][j])
            #print(i,j)
            if 0 <= i <= 7 and 0 <= j <= 7 and board[i][j] == mark:
                if j+1 == 8 or board[i][j+1] != " ":
                    while 0 <= j <= 7 and 0 <= i <= 7 and board[i][j] == mark:
                        checker += 1
                        #i += 1
                        j += 1
                        #print(i,j)
                    #print(checker)
                    if checker == 5:
                        return True
                    else:
                        checker = 0
                    #checker += 1

                else:
                    if checker == 5:
                        return True
                    else:
                        checker = 0
    return False

def is_col_all_marks(board, mark):
    checker = 0
    for i in range(len(board)):
        for j in range(len(board)):
            #print(board[i][j])
            #print(i,j)
            #while 0 <= j <= 7 and 0 <= i <= 7:
            if 0 <= i <= 7 and 0 <= j <= 7 and board[i][j] == mark:
                if i+1 == 8 or board[i+1][j] != " ":
                    while 0 <= i <= 7 and 0 <= j <= 7 and board[i][j] == mark:
                        checker += 1
                        #i += 1
                        i += 1
                        #print(i,j)
                    #print(checker)
                    if checker == 5:
                        return True
                    else:
                        checker = 0

#                 else:
#                     if checker == 5:
#                         return True
#                     else:
#                         checker = 0
    return False

def is_upper_left_all_marks(board, mark):
    checker = 0
    for i in range(len(board)):
        for j in range(len(board)):
            #print(board[i][j])
            #print(i,j)
            if 0 <= i <= 7 and 0 <= j <= 7 and board[i][j] == mark:
                if i+1 == 8 or j+1 == 8 or board[i+1][j+1] != " ":
                    while 0 <= i <= 7 and 0 <= j <= 7 and board[i][j] == mark:
                        checker += 1
                        #i += 1
                        i += 1
                        j+= 1
                    #print(checker)
                    if checker == 5:
                        return True
                    else:
                        checker = 0

                else:
                    if checker == 5:
                        return True
                    else:
                        checker = 0
    return False

def is_upper_right_all_marks(board, mark):
    checker = 0
    for i in range(len(board)):
        for j in range(len(board)):
            #print(board[i][j])
            #print(i,j)
            if 0 <= i <= 7 and 0 <= j <= 7 and board[i][j] == mark:
                if i+1 == 8 or j-1 == 8 or board[i+1][j-1] != " ":
                    while 0 <= i <= 7 and 0 <= j <= 7 and board[i][j] == mark:
                        checker += 1
                        #i += 1
                        i += 1
                        j+= -1
                    #print(checker)
                    if checker == 5:
                        return True
                    else:
                        checker = 0
    return False

def is_win(board):
    for i in range(len(board)):
        if is_row_all_marks(board, "b") == True or is_col_all_marks(board, "b") == True or is_upper_left_all_marks(board, "b") == True or is_upper_right_all_marks(board, "b"):
            return "Black won"
        elif is_row_all_marks(board, "w") == True or is_col_all_marks(board, "w") == True or is_upper_left_all_marks(board, "w") == True or is_upper_right_all_marks(board, "w"):
            return "White won"
        else:
            return "Keep playing"




def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board



def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))






def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res





        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res



def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3; x = 5; d_x = -1; d_y = 1; length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #

    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0




if __name__ == '__main__':
    #play_gomoku(8)
    #board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['b', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', 'b', ' ', ' ', ' ', ' ', ' '], [' ', 'b', 'b', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', 'b', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', 'b', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', 'b', ' ']]
    #board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['b', 'b', ' ', ' ', 'w', 'w', 'w', 'w'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['w', 'w', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    board = [[' ', ' ', ' ', ' ', ' ', 'w', 'b', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', 'b', ' ', ' ', ' '], [' ', ' ', ' ', 'b', ' ', ' ', ' ', ' '], [' ', 'w', 'b', ' ', ' ', ' ', ' ', ' '], [' ', 'w', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 'w', ' ', ' ', ' ', ' ', ' ', ' ']]

    print_board(board)
    #print(is_bounded(board, 5, 2, 3, 1, -1))
    #print(detect_row(board, "b", 7, 0, 3, 1, 0))
    #print(detect_row(board, "w", 0, 7, 3, 1, 0))
    #print(detect_rows(board, "w", 3))
    #print(detect_row(board, "X", 1, 0, 2, 0, 1))
    #print(detect_rows(board, "w", 4))
    #print(is_win(board))
    #print(score)
    #print(search_max(board))
    #easy_testset_for_main_functions()
#     board[0][5] = "w"
#     board[0][6] = "b"
    #some_tests()
    play_gomoku(8)

