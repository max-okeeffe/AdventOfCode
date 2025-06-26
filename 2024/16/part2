import numpy as np

filename = input() + ".txt"
map = open(filename).read().split('\n')

m, n = len(map), len(map[0])
X = np.array([map[i][j] for i in range(m) for j in range(n)]).reshape(m,n)

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

def neis(node):
    pos, dir = node
    out = []
    u,v = pos[0] + dir[0], pos[1] + dir[1]
    if X[u,v] != '#':
        out.append( ((u,v),dir) )
    
    if dir in [(0,1), (0,-1)]:
        for d in [(1,0), (-1,0)]:
            u, v = pos[0] + d[0], pos[1] + d[1]
            if X[u,v] != '#':
                out.append((pos,d))
    else:
        for d in [(0,1), (0,-1)]:
            u, v = pos[0] + d[0], pos[1] + d[1]
            if X[u,v] != '#':
                out.append((pos,d))
    
    return out

def weight(node,nei):
    if node[1] == nei[1]:
        return 1
    return 1000

dirs = ((1,0),(-1,0),(0,1),(0,-1))
nodes = [ ((a,b),(c,d)) for a in range(m) for b in range(n) if X[a,b] != '#' for (c,d) in dirs ]
start = ((a,b),(0,1))
dots = {(i,j) for i in range(m) for j in range(n) if X[i,j] != '#'}

def flip(d):
    return (-d[0], -d[1])
            
def dijkstra(start):
    d, Q = {}, []
    for node in nodes:
        d[node] = float('inf')
        Q.append(node)
    d[start] = 0
    Q.remove(start)
    Q.append(start)

    while Q:
        minn = Q[-1]
        i = len(Q) - 1
        while d[Q[i]] < float('inf') and i >= 0:
            if d[Q[i]] < d[minn]:
                minn = Q[i]
            i -= 1
        Q.remove(minn)

        for nei in neis(minn):
            temp = d[minn] + weight(minn,nei)
            if temp < d[nei]:
                d[nei] = temp
                Q.remove(nei)
                Q.append(nei)

    return d

d1, d2 = dijkstra(start), dijkstra(((x,y),(1,0)))
count = 0
for dot in dots:
    for d in dirs:
        if d1[(dot,d)] + d2[(dot,flip(d))] == 99460:
            count += 1
            break

print(count)
