import numpy as np

filename = input() + ".txt"
board, moves = open(filename).read().split('\n\n')
board = board.split('\n')

m, n = len(board), len(board[0])
X = np.array([board[i][j] for i in range(m) for j in range(n)]).reshape(m,n)

a, b = 0, 0
while board[a][b] != '@':
    b += 1
    if b == n:
        a += 1
        b = 0

for move in moves:

    if move == '^':
        if X[a-1,b] == '.':
            X[a,b], X[a-1,b] = '.', '@'
            a -= 1
        else:
            i = a-1
            while X[i,b] == 'O':
                i -= 1
            if X[i,b] == '.':
                X[a,b], X[a-1,b], X[i,b] = '.', '@', 'O'
                a -= 1

    if move == 'v':
        if X[a+1,b] == '.':
            X[a,b], X[a+1,b] = '.', '@'
            a += 1
        else:
            i = a+1
            while X[i,b] == 'O':
                i += 1
            if X[i,b] == '.':
                X[a,b], X[a+1,b], X[i,b] = '.', '@', 'O'
                a += 1

    if move == '<':
        if X[a,b-1] == '.':
            X[a,b], X[a,b-1] = '.', '@'
            b -= 1
        else:
            j = b-1
            while X[a,j] == 'O':
                j -= 1
            if X[a,j] == '.':
                X[a,b], X[a,b-1], X[a,j] = '.', '@', 'O'
                b -= 1

    if move == '>':
        if X[a,b+1] == '.':
            X[a,b], X[a,b+1] = '.', '@'
            b += 1
        else:
            j = b+1
            while X[a,j] == 'O':
                j += 1
            if X[a,j] == '.':
                X[a,b], X[a,b+1], X[a,j] = '.', '@', 'O'
                b += 1

for i in range(m):
    print(''.join(X[i,j] for j in range(n)))

print( sum( 100 * i + j for i in range(m) for j in range(n) if X[i,j] == 'O' ) )
