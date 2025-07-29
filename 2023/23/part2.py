from collections import deque

filename = input() + ".txt"
plan = open(filename).read().split('\n')

m, n, a, b = len(plan), len(plan[0]), plan[0].index('.'), plan[-1].index('.')

nodes = [(i,j) for i in range(m) for j in range(n) if plan[i][j] != '#']
neis = {}
for i,j in nodes:
    for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
        if 0 <= x < m and 0 <= y < n and plan[x][y] != '#':
            neis.setdefault((i,j), set()).add(((x,y),1))
            neis.setdefault((x,y), set()).add(((i,j),1))

while True:
    for node, edges in neis.items():
        if len(edges) == 2:
            item1, item2 = edges
            nei1, d1 = item1
            nei2, d2 = item2
            neis[nei1].remove((node,d1))
            neis[nei2].remove((node,d2))
            neis[nei1].add((nei2,d1+d2))
            neis[nei2].add((nei1,d1+d2))
            del neis[node]
            break
    else:
        break

Q, visited, maxd = deque(), set(), 0
Q.append(((0,a),0))
while Q:
    node, d = Q.pop()
    if d == -1:
        visited.remove(node)
        continue
    if node == (m-1,b):
        maxd = max(maxd,d)
        continue
    if node in visited:
        continue
    visited.add(node)
    Q.append((node,-1))
    for nei, e in neis[node]:
        Q.append((nei,d+e))

print(maxd)
