import gameover
import boardeval
import getmove
import printboard


if __name__ == "__main__":
    DRAW = 0
    USER = 1
    COMPUTER = 2
    board = [0]*42
    while 1:
        printboard.printboard(board)
        user_move = int(input('Enter your move'))
        getmove.make_move(board, user_move, USER)
        game_state = gameover.gameover(board)
        if game_state == USER:
            printboard.printboard(board)
            print('Human-1:Computer-0')
            break
        elif game_state == DRAW:
            printboard.printboard(board)
            print('Draw')
            break
        else:
            getmove.make_move(board, getmove.getmove(board, COMPUTER), COMPUTER)
            game_state = gameover.gameover(board)
            if game_state == COMPUTER:
                printboard.printboard(board)
                print('Computer-1:Human-0')
                break
            elif game_state == DRAW:
                printboard.printboard(board)
                print('Draw')
