from heapq import heapify, heappop, heappush

filename = input() + ".txt"
plan = open(filename).read().split('\n')

m,n = len(plan), len(plan[0])

def find(val):
    for i in range(m):
        for j in range(n):
            if plan[i][j] == val:
                return i, j

start = find('S')
end = find('E')

def val(x):
    if x == 'S':
        return ord('a')
    if x == 'E':
        return ord('z')
    return ord(x)

def neis(node):
    i, j = node
    return [(x,y) for x,y in ((i+1,j), (i-1,j), (i,j+1), (i,j-1)) if 0 <= x < m and 0 <= y < n and val(plan[x][y]) - val(plan[i][j]) <= 1]

dis = {(i,j) : float('inf') for i in range(m) for j in range(n)}
dis[start] = 0

Q = [(0,start)]
heapify(Q)
visited = set()

while Q:
    d, minn = heappop(Q)

    if minn in visited:
        continue
    visited.add(minn)

    for nei in neis(minn):
        temp = d + 1
        if temp < dis[nei]:
            dis[nei] = temp
            heappush(Q, (temp, nei))
    
print(dis[end])
