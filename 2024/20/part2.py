import numpy as np

filename = input() + ".txt"
track = open(filename).read().split('\n')

m, n = len(track), len(track[0])
X = np.array([track[i][j] for i in range(m) for j in range(n)]).reshape(m,n)

a, b = 0, 0
while X[a,b] != 'S':
    b += 1
    if b == n:
        a += 1
        b = 0

x, y = 0, 0
while X[x,y] != 'E':
    y += 1
    if y == n:
        x += 1
        y = 0

curr = (a,b)
path = [curr]

while curr != (x,y):
    i, j = curr
    for nei_i, nei_j in ((i+1,j), (i-1,j), (i,j+1), (i,j-1)):
        if X[nei_i,nei_j] != '#' and (nei_i,nei_j) not in path:
            curr = (nei_i,nei_j)
            path.append(curr)
            break

N = len(path)
count = 0
for i in range(N-2):
    for j in range(i+2,N):
        a,b = path[i]
        x,y = path[j]
        k = abs(a-x) + abs(b-y)
        if k <= 20 and j - i - k >= 100:
            count += 1

print(count)
