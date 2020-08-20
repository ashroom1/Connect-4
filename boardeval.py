board_value = 0
board_matrix = 0


count = 0


def evaluate_value(who):
    global board_matrix
    current_value = 0
    for i in range(7):
        for j in range(6):
            if board_matrix[j][i] == str(who):
                current_value += check_all(str(who), i, j)
                if current_value == 5000:
                    return current_value
    return current_value


def check_all(who, x, y):
    ONE = 1
    TWO = 50
    THREE = 100
    FOUR = 5000
    four_squares = []
    current_value = 0
    for i in range(4):  # check right horizontal
        if (x+i) >= 7 or board_matrix[y][x+i] == str(3-int(who)):
            break
        four_squares.append(board_matrix[y][x+i])
    if len(four_squares) < 4:
        pass
    else:
        current_value += ONE
        if four_squares[1] == who:
            current_value -= 1
            current_value += TWO
            if four_squares[2] == who:
                current_value += THREE
                if four_squares[3] == who:
                    return FOUR
    four_squares = []
    for j in range(4):  # check left horizontal
        if (x-j) < 0 or board_matrix[y][x-j] == str(3-int(who)):
            break
        four_squares.append(board_matrix[y][x-j])
    if len(four_squares) < 4:
        pass
    else:
        current_value += ONE
        if four_squares[1] == who:
            current_value -= 1
            current_value += TWO
            if four_squares[2] == who:
                current_value += THREE
                if four_squares[3] == who:
                    return FOUR
    four_squares = []
    for i in range(4):  # check vertical
        if (y+i) >= 6 or board_matrix[y+i][x] == str(3-int(who)):
            break
        four_squares.append(board_matrix[y+i][x])
    if len(four_squares) < 4:
        pass
    else:
        current_value += ONE
        if four_squares[1] == who:
            current_value -= 1
            current_value += TWO
            if four_squares[2] == who:
                current_value += THREE
                if four_squares[3] == who:
                    return FOUR
    four_squares = []
    for i in range(4):  # check left down
        if ((y-i) < 0) or ((x-i) < 0) or board_matrix[y-i][x-i] == str(3-int(who)):
            break
        four_squares.append(board_matrix[y-i][x-i])
    if len(four_squares) < 4:
        pass
    else:
        current_value += ONE
        if four_squares[1] == who:
            current_value -= 1
            current_value += TWO
            if four_squares[2] == who:
                current_value += THREE
                if four_squares[3] == who:
                    return FOUR
    four_squares = []
    for i in range(4):  # check left up
        if ((y+i) >= 6) or ((x-i) < 0) or board_matrix[y+i][x-i] == str(3-int(who)):
            break
        four_squares.append(board_matrix[y+i][x-i])
    if len(four_squares) < 4:
        pass
    else:
        current_value += ONE
        if four_squares[1] == who:
            current_value -= 1
            current_value += TWO
            if four_squares[2] == who:
                current_value += THREE
                if four_squares[3] == who:
                    return FOUR
    four_squares = []
    for i in range(4):
        if ((y-i) < 0) or ((x+i) >= 7) or board_matrix[y-i][x+i] == str(3-int(who)): # check right down
            break
        four_squares.append(board_matrix[y-i][x+i])
    if len(four_squares) < 4:
        pass
    else:
        current_value += ONE
        if four_squares[1] == who:
            current_value -= 1
            current_value += TWO
            if four_squares[2] == who:
                current_value += THREE
                if four_squares[3] == who:
                    return FOUR
    four_squares = []
    for i in range(4):  # check right up
        if ((y+i) >= 6) or ((x+i) >= 7) or board_matrix[y+i][x+i] == str(3-int(who)):
            break
        four_squares.append(board_matrix[y+i][x+i])
    if len(four_squares) < 4:
        pass
    else:
        current_value += ONE
        if four_squares[1] == who:
            current_value -= 1
            current_value += TWO
            if four_squares[2] == who:
                current_value += THREE
                if four_squares[3] == who:
                    return FOUR
    four_squares = []
    return current_value


def convert_to_matrix(board_string):
    global board_matrix, count
    board_matrix = [[0 for x in range(7)] for y in range(6)]
    for i in range(6):
        for j in range(7):
            board_matrix[i][j] = board_string[count]
            count += 1
    count = 0


def boardeval(board, who):
    global board_value, board_matrix
    board_list = [str(x) for x in board]
    board_string = "".join(board_list)
    convert_to_matrix(board_string)
    board_value = evaluate_value(who)
    if who == 2:
        return -board_value
    return board_value
