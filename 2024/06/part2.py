from copy import deepcopy

filename = input() + ".txt"

start_map = [[char for char in row] for row in open(filename).read().split('\n')]

m = len(start_map[0])
n = len(start_map)

start_i, start_j = 0, 0

while start_map[start_j][start_i] != '^':
    start_i += 1
    if start_i == m:
        start_i = 0
        start_j += 1

i,j,k=start_i, start_j, 0
dirs = [(0,-1), (1,0), (0,1), (-1,0)]
nei_i, nei_j = i + dirs[k][0], j + dirs[k][1]
path = []

while 0 <= nei_i < m and 0 <= nei_j < n:
    if start_map[nei_j][nei_i] == '#':
        k = (k + 1) % 4
        nei_i, nei_j = i + dirs[k][0], j + dirs[k][1]
    else:
        i, j, nei_i, nei_j = nei_i, nei_j, i + dirs[k][0], j + dirs[k][1]
        if (i,j) not in path:
            path.append((i,j))

count = 0
for index, place in enumerate(path):
    print(index)
    a,b = place
    start_map[b][a] = '#'

    i,j,k = start_i, start_j, 0
    nei_i, nei_j = i + dirs[k][0], j + dirs[k][1]
    visited = [(i,j,k)]

    while 0 <= nei_i < m and 0 <= nei_j < n:
        if start_map[nei_j][nei_i] == '#':
            k = (k + 1) % 4
            nei_i, nei_j = i + dirs[k][0], j + dirs[k][1]
        else:
            i,j,nei_i,nei_j = nei_i,nei_j, nei_i + dirs[k][0], nei_j + dirs[k][1]
        
        if (i,j,k) in visited:
            count += 1
            start_map[b][a] = '.'
            break
        else:
            visited.append((i,j,k))
    start_map[b][a] = '.'

print(count)
