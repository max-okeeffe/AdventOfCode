filename = input() + ".txt"

board = open(filename).read().split('\n')
n = len(board)

verticals = [''.join(board[k][i] for k in range(n)) for i in range(n)]
diagonals1 = [''.join(board[k-i][i] for i in range(max(0,k-n+1),min(k,n-1)+1)) for k in range(2*n-1)]
diagonals2 = [''.join(board[n-k+i-1][i] for i in range(max(0,k-n+1),min(k,n-1)+1)) for k in range(2*n-1)]

print(sum(row.count("XMAS") + row.count("SAMX") for row in board + verticals + diagonals1 + diagonals2))
