import numpy as np

filename = input() + ".txt"
bytes = list(map(lambda x : list(map(int, x.split(','))), open(filename).read().split('\n')))

X = np.zeros((71,71), dtype = int)
for i, j in bytes[:1024]:
    X[i,j] = 1

start, end = (0,0), (70,70)
nodes = [(i,j) for i in range(71) for j in range(71) if X[i,j] == 0]

def neis(node):
    i,j = node
    return [(a,b) for a,b in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)) if 0 <= a <= 70 and 0 <= b <= 70 and X[a,b] == 0]

def h(node):
    return 138 - node[0] - node[1]

def astar():
    f, g, open, closed = {}, {}, [], []
    for node in nodes:
        f[node] = float('inf')
    f[start], g[start] = 0, 0
    open.append(start)

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

            temp = g[minn] + 1

            if nei not in open:
                f[nei] = temp + h(nei)
                g[nei] = temp
                open.append(nei)
            elif temp < g[nei]:
                f[nei] = temp + h(nei)
                g[nei] = temp

    return float('inf')

print(astar())
