filename = input() + ".txt"

board = open(filename).read().split('\n')
n = len(board)

print(
    sum( 1 for i in range(1,n-1) for j in range(1,n-1)
        if board[j][i] == 'A'
        and {board[j-1][i-1], board[j+1][i+1]} == {'M','S'}
        and {board[j-1][i+1], board[j+1][i-1]} == {'M','S'}
        )
    )
