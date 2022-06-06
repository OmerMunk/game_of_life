alive = chr(9608)
dead = chr(9617)

size = 30

board = [[dead for i in range(size)] for j in range(size)]

def printer(board):
    ret_val = ""
    for row in board:
        ret_val += "  ".join(row) + "\n"
    return ret_val


def init_board(board, *lists):
    for a in lists:
        x = a[0]
        y = a[1]
        board[x][y] = alive
    return board


def check(board, row, col, count):
    if row == 0 and col == 0:
        return zero_zero_check(board, row, col, count)
    if row == 0 and col == size - 1:
        return zero_size_check(board, row, col, count)
    if row == size - 1 and col == size - 1:
        return size_size_check(board, row, col, count)
    if row == size - 1 and col == 0:
        return size_zero_check(board, row, col, count)
    if row == 0:
        return first_row_base_check(board, row, col, count)
    if row == size - 1:
        return last_row_base_check(board, row, col, count)
    if col == 0:
        return first_column_base_check(board, row, col, count)
    if col == size - 1:
        return last_column_base_check(board, row, col, count)
    else:
        return base_check(board, row, col, count)


def base_check(board, row, col, count):
    count = check_up(board, row, col, count)
    count = check_up_right(board, row, col, count)
    count = check_right(board, row, col, count)
    count = check_down_right(board, row, col, count)
    count = check_down(board, row, col, count)
    count = check_left_down(board, row, col, count)
    count = check_left(board, row, col, count)
    count = check_up_left(board, row, col, count)
    return count


def first_row_base_check(board, row, col, count):
    count = check_right(board, row, col, count)
    count = check_down_right(board, row, col, count)
    count = check_down(board, row, col, count)
    count = check_left_down(board, row, col, count)
    count = check_left(board, row, col, count)
    return count


def zero_zero_check(board, row, col, count):
    count = check_right(board, row, col, count)
    count = check_down_right(board, row, col, count)
    count = check_down(board, row, col, count)
    return count


def zero_size_check(board, row, col, count):
    count = check_down(board, row, col, count)
    count = check_left_down(board, row, col, count)
    count = check_left(board, row, col, count)
    return count


def last_row_base_check(board, row, col, count):
    count = check_up(board, row, col, count)
    count = check_up_right(board, row, col, count)
    count = check_right(board, row, col, count)
    count = check_left(board, row, col, count)
    count = check_up_left(board, row, col, count)
    return count


def size_zero_check(board, row, col, count):
    count = check_up(board, row, col, count)
    count = check_up_right(board, row, col, count)
    count = check_right(board, row, col, count)
    return count


def size_size_check(board, row, col, count):
    count = check_up(board, row, col, count)
    count = check_left(board, row, col, count)
    count = check_up_left(board, row, col, count)
    return count


def first_column_base_check(board, row, col, count):
    count = check_up(board, row, col, count)
    count = check_up_right(board, row, col, count)
    count = check_right(board, row, col, count)
    count = check_down_right(board, row, col, count)
    count = check_down(board, row, col, count)
    return count


def last_column_base_check(board, row, col, count):
    count = check_up(board, row, col, count)
    count = check_down(board, row, col, count)
    count = check_left_down(board, row, col, count)
    count = check_left(board, row, col, count)
    count = check_up_left(board, row, col, count)
    return count


def check_up(board, row, col, count):
    if board[row - 1][col] == alive:
        count += 1
    return count


def check_up_left(board, row, col, count):
    if board[row - 1][col - 1] == alive:
        count += 1
    return count


def check_up_right(board, row, col, count):
    if board[row - 1][col + 1] == alive:
        count += 1
    return count


def check_left(board, row, col, count):
    if board[row][col - 1] == alive:
        count += 1
    return count


def check_left_down(board, row, col, count):
    if board[row + 1][col - 1] == alive:
        count += 1
    return count


def check_down(board, row, col, count):
    if board[row + 1][col] == alive:
        count += 1
    return count


def check_down_right(board, row, col, count):
    if board[row + 1][col + 1] == alive:
        count += 1
    return count


def check_right(board, row, col, count):
    if board[row][col + 1] == alive:
        count += 1
    return count


def next_status(board, row, col):
    count = 0
    if board[row][col] == alive:
        count = check(board, row, col, count)
        if count not in [2, 3]:
            return dead
        else:
            return alive

    elif board[row][col] == dead:
        count = check(board, row, col, count)
        if count == 3:
            return alive
        else:
            return dead


def next_step(board):
    next_board = [[dead for i in range(size)] for j in range(size)]
    for row in range(size):
        for col in range(size):
            next_board[row][col] = next_status(board, row, col)
    return next_board


# board = init_board(board,[2,3],[1,3],[1,4],[0,4],[0,2], [10,12], [9,12], [8,11], [8,13], [9,13], [6,19], [5,19], [4,19], [6,20], [6,17], [8,19], [8,18], [26,16], [27,16], [27,17], [26,17])
board = init_board(board, [15, 15], [14, 15], [16, 15], [15, 14], [14, 16])
print(printer(board))
print()
board = next_step(board)
print(printer(board))
print()
x = input("enter to next, anything else to stop\n")
while x == "":
    board = next_step(board)
    print(printer(board))
    x = input("enter to next, anything else to stop\n")
