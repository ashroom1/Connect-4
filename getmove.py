from boardeval import boardeval
import copy


def make_move(board, position, who):
    for i in range(6):
        if board[position+(7*i)] == 0:
            board[position+(7*i)] = who
            return board


def remove_move(board, position):
    for i in [5, 4, 3, 2, 1, 0]:
        if board[position+(7*i)] != 0:
            board[position+(7*i)] = 0
            return board


def getmove(board, who):
    local_board = copy.deepcopy(board)
    current_best_move = 0
    current_best_score = 0
    for x in range(1, 8):
        if local_board[-x] == 0:
            if current_best_score == 0:
                current_best_move = 7-x
                current_best_score = boardeval(local_board, who)+best_value(local_board, 3-who)
            local_board = make_move(local_board, 7-x, who)
            if abs(boardeval(local_board, who)) == 5000:
                return 7-x
            if (boardeval(local_board, who)+best_value(local_board, 3-who))*(-1 if who == 2 else 1) > current_best_score*(-1 if who == 2 else 1):
                current_best_score = boardeval(local_board, who)+best_value(local_board, 3-who)
                current_best_move = 7-x
            local_board = remove_move(local_board, 7-x)
    return current_best_move


def best_value(board, who):
    local_board = copy.deepcopy(board)
    current_best_score = 0
    for x in range(1, 8):
        if local_board[-x] == 0:
            if current_best_score == 0:
                current_best_score = boardeval(local_board, who)
            local_board = make_move(local_board, 7-x, who)
            if boardeval(local_board, who)*(-1 if who == 2 else 1) > current_best_score*(-1 if who == 2 else 1):
                current_best_score = boardeval(local_board, who)
            local_board = remove_move(local_board, 7-x)
    return current_best_score






