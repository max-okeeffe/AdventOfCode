from math import prod

filename = input() + ".txt"
plan = open(filename).read().split('\n')

m, n = len(plan), len(plan[0])

a, b = 0, 0
while plan[a][b] != 'S':
    b += 1
    if b == n:
        b = 0
        a += 1

def neis(i,j):
    return [(x,y) for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)) if plan[x % m][y % n] != '#']

boundaries, d, seq = [[(a,b)], neis(a,b)], {0 : 1, 1 : len(neis(a,b))}, []
for k in range(2,65 + 2 * 131 + 1):
    checked = boundaries.pop(0)
    oldboundary, newboundary = boundaries[0], []
    for i, j in oldboundary:
        for x, y in neis(i,j):
            if (x,y) not in checked and (x,y) not in newboundary:
                newboundary.append((x,y))
    boundaries.append(newboundary)
    d[k] = len(newboundary) + d[k-2]

seq, N = [d[65], d[65 + 131], d[65 + 2 * 131]], (26501365 - 65) // 131

print(sum(seq[j] * prod(N-i for i in range(3) if i != j) // prod(j-i for i in range(3) if i != j) for j in range(3)))
