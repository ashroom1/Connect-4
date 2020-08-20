def printboard(board):
    count = 1
    for i in range(6):
        for j in range(7):
            print(board[-(count+(6-j))], end="")
        count += 7
        print()
