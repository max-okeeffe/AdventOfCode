import numpy as np

filename = input() + ".txt"
board, moves = open(filename).read().split('\n\n')
board = board.split('\n')

newboard = []
for row in board:
    newstring = ''
    for x in row:
        if x == '#':
            newstring += '##'
        elif x == 'O':
            newstring += '[]'
        elif x == '.':
            newstring += '..'
        else:
            newstring += '@.'
    newboard.append(newstring)

m, n = len(newboard), len(newboard[0])
X = np.array([newboard[i][j] for i in range(m) for j in range(n)]).reshape(m,n)

a, b = 0, 0
while X[a,b] != '@':
    b += 1
    if b == n:
        a += 1
        b = 0

for move in moves:

    if move == '^':
        if X[a-1,b] == '.':
            X[a,b], X[a-1,b] = '.', '@'
            a -= 1
        elif X[a-1,b] != '#':
            levels = []
            if X[a-1,b] == '[':
                levels.append([(a-1,b)])
            elif X[a-1,b] == ']':
                levels.append([(a-1,b-1)])
            while all(X[i-1,j] != '#' and X[i-1,j+1] != '#' for (i,j) in levels[-1]) and any(X[i-1,j] != '.' or X[i-1,j+1] != '.' for (i,j) in levels[-1]):
                temp = []
                for (i,j) in levels[-1]:
                    if X[i-1,j] == '[':
                        temp.append((i-1,j))
                    elif X[i-1,j] == ']':
                        temp.append((i-1,j-1))
                    if X[i-1,j+1] == '[':
                        temp.append((i-1,j+1))
                levels.append(temp)
            if all(X[i-1,j] == '.' and X[i-1,j+1] == '.' for (i,j) in levels[-1]):
                for k in range(len(levels)-1, -1, -1):
                    for (i,j) in levels[k]:
                        X[i-1,j], X[i-1,j+1], X[i,j], X[i,j+1] = '[', ']', '.', '.'
                X[a,b], X[a-1,b] = '.', '@'
                a -= 1

    if move == 'v':
        if X[a+1,b] == '.':
            X[a,b], X[a+1,b] = '.', '@'
            a += 1
        elif X[a+1,b] != '#':
            levels = []
            if X[a+1,b] == '[':
                levels.append([(a+1,b)])
            elif X[a+1,b] == ']':
                levels.append([(a+1,b-1)])
            while all(X[i+1,j] != '#' and X[i+1,j+1] != '#' for (i,j) in levels[-1]) and any(X[i+1,j] != '.' or X[i+1,j+1] != '.' for (i,j) in levels[-1]):
                temp = []
                for (i,j) in levels[-1]:
                    if X[i+1,j] == '[':
                        temp.append((i+1,j))
                    elif X[i+1,j] == ']':
                        temp.append((i+1,j-1))
                    if X[i+1,j+1] == '[':
                        temp.append((i+1,j+1))
                levels.append(temp)
            if all(X[i+1,j] == '.' and X[i+1,j+1] == '.' for (i,j) in levels[-1]):
                for k in range(len(levels)-1, -1, -1):
                    for (i,j) in levels[k]:
                        X[i+1,j], X[i+1,j+1], X[i,j], X[i,j+1] = '[', ']', '.', '.'
                X[a,b], X[a+1,b] = '.', '@'
                a += 1

    if move == '<':
        if X[a,b-1] == '.':
            X[a,b], X[a,b-1] = '.', '@'
            b -= 1
        elif X[a,b-1] != '#':
            j = b-1
            while X[a,j] in ('[', ']'):
                j -= 1
            if X[a,j] == '.':
                X[a,b], X[a,b-1] = '.', '@'
                for e, v in enumerate(range(j,b-1)):
                    X[a,v] = ('[', ']')[e % 2]
                b -= 1

    if move == '>':
        if X[a,b+1] == '.':
            X[a,b], X[a,b+1] = '.', '@'
            b += 1
        elif X[a,b+1] != '#':
            j = b+1
            while X[a,j] in ('[', ']'):
                j += 1
            if X[a,j] == '.':
                X[a,b], X[a,b+1] = '.', '@'
                for e, v in enumerate(range(b+2,j+1)):
                    X[a,v] = ('[', ']')[e % 2]
                b += 1

for i in range(m):
    print(''.join(X[i,j] for j in range(n)))

print( sum( 100 * i + j for i in range(m) for j in range(n) if X[i,j] == '[' ) )
