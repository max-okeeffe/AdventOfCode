from collections import deque

#filename = input() + ".txt"
filename = "data.txt"
plan = open(filename).read().split('\n')

m, n, a, b = len(plan), len(plan[0]), plan[0].index('.'), plan[-1].index('.')
u, d, l, r = '^', 'v', '<', '>'

def neis(i,j,dir):
    val = plan[i][j]
    if val == r:
        return [(i,j+1,r)]
    if val == d:
        return [(i+1,j,d)]
    if val == l:
        return [(i,j-1,l)]
    if val == u:
        return [(i-1,j,u)]
    
    baddir = '^' if dir == 'v' else 'v' if dir == '^' else '<' if dir == '>' else '>'
    poss = [(x,y,dir1) for x, y, dir1 in ((i+1,j,d),(i-1,j,u),(i,j+1,r),(i,j-1,l)) if 0 <= x < m and 0 <= y < n and dir1 != baddir]
    valid = []
    for x, y, dir1 in poss:
        val = plan[x][y]
        if val == '.':
            valid.append((x,y,dir1))
        elif val == r and y == j+1:
            valid.append((x,y,dir1))
        elif val == d and x == i+1:
            valid.append((x,y,dir1))
        elif val == l and y == j-1:
            valid.append((x,y,dir1))
        elif val == u and y == i-1:
            valid.append((x,y,dir1))
    return valid

dis, Q = {(a,0,d) : 0}, deque()
Q.append((a,0,d))
while Q:
    node = Q.popleft()
    for nei in neis(*node):
        dis[nei] = dis[node] + 1
        Q.append(nei)

print(dis[(m-1,b,d)])
