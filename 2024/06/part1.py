filename = input() + ".txt"

map = open(filename).read().split('\n')
m = len(map[0])
n = len(map)

i,j = 0, 0
while map[j][i] != '^':
    i += 1
    if i == m:
        i = 0
        j += 1

k = 0
dirs = [(0,-1), (1,0), (0,1), (-1,0)]
nei_i, nei_j = i + dirs[k][0], j + dirs[k][1]
visited = [(i,j)]

while 0 <= nei_i < m and 0 <= nei_j < n:
    if map[nei_j][nei_i] == '#':
        k = (k + 1) % 4
        nei_i, nei_j = i + dirs[k][0], j + dirs[k][1]
    else:
        i, j, nei_i, nei_j = nei_i, nei_j, nei_i + dirs[k][0], nei_j + dirs[k][1]
        if (i,j) not in visited:
            visited.append((i,j))

print(len(visited))
