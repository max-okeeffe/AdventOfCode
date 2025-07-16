from heapq import heappush, heappop

filename = input() + ".txt"
plan = [[int(x) for x in row] for row in open(filename).read().split('\n')]

m, n = len(plan), len(plan[0])

def neis(node):
    i,j,x,y = node
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    dirs.remove((-x,-y))
    dirs.remove((x,y))
    return [(i+k*dx,j+k*dy,dx,dy) for dx, dy in dirs for k in range(4,11) if 0 <= i+k*dx < m and 0 <= j+k*dy < n]

def weight(node, nei):
    a,b,*_ = node
    x,y,dx,dy = nei
    k = max(abs(x-a), abs(y-b))
    return sum(plan[a+i*dx][b+i*dy] for i in range(1,k+1))

nodes = [(i,j,x,y) for i in range(m) for j in range(n) for x, y in ((1,0),(0,1),(0,-1),(-1,0))]

def dijkstra(start):
    Q, d = [], {}
    for node in nodes:
        d[node] = float('inf')
    d[start] = 0
    heappush(Q, (0,start))

    while Q:
        minn = heappop(Q)[1]
        for nei in neis(minn):
            val = d[minn] + weight(minn,nei)
            if d[nei] > val:
                d[nei] = val
                heappush(Q,(val,nei))

    return min(d[(m-1,n-1,0,1)], d[(m-1,n-1,1,0)])

print(min(dijkstra((0,0,0,1)), dijkstra((0,0,1,0))))
