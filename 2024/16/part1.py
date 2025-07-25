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

def h(node1,node2):
    pos1, pos2 = node1[0], node2[0]
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

dirs = ((1,0),(-1,0),(0,1),(0,-1))
nodes = [ ((a,b),(c,d)) for a in range(m) for b in range(n) if X[a,b] != '#' for (c,d) in dirs ]
start = ((a,b),(0,1))

def astar(end):
    f, g = {}, {}
    for node in nodes:
        f[node] = float('inf')
        g[node] = 0

    f[start], g[start] = h(start,end), 0

    open, closed = [start], []
    while open:
        minn = open[0]
        for node in open:
            if f[node] < f[minn]:
                minn = node

        if minn == end:
            return g[minn]

        open.remove(minn)
        closed.append(minn)

        for nei in neis(minn):
            if nei in closed:
                continue
            temp = g[minn] + weight(minn,nei)
            if nei not in open:
                g[nei] = temp
                f[nei] = temp + h(nei,end)
                open.append(nei)
            elif temp < g[nei]:
                g[nei] = temp
                f[nei] = temp + h(nei,end)
    return float("inf")

print( min(astar(((x,y),d)) for d in dirs) )
