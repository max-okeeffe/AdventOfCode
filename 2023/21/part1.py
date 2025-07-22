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
    return [(x,y) for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)) if 0 <= x < m and 0 <= y < n and plan[x][y] != '#']

level = {(a,b)}
for _ in range(64):
    temp = set()
    for i, j in level:
        for x, y in neis(i,j):
            temp.add((x,y))
    level = temp

print(len(level))
