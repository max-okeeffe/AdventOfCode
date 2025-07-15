filename = input() + ".txt"
plan = open(filename).read().split('\n')

m, n = len(plan), len(plan[0])
a, b = 0, 0
while plan[a][b] != 'S':
    b += 1
    if b == n:
        b = 0
        a += 1

entries = []
if a > 0 and plan[a-1][b] in '|7F':
    entries.append((a-1,b))
if a < m-1 and plan[a+1][b] in '|LJ':
    entries.append((a+1,b))
if b > 0 and plan[a][b-1] in '-FL':
    entries.append((a,b-1))
if b < n-1 and plan[a][b+1] in '-J7':
    entries.append((a,b+1))

def loc(oldx, x, pipe):
    a,b = x
    i,j = oldx
    di, dj = a-i, b-j

    if pipe in '-|':
        return (a+di,b+dj)
    
    if pipe in 'L7':
        return (a+dj,b+di)
    
    return (a-dj,b-di)

x, y = entries
oldx, oldy, i = (a,b), (a,b), 1
v1, v2 = [] if plan[a][b] in '-|' else [(a,b)], []
while x != y:
    i += 1
    xpipe = plan[x[0]][x[1]]
    if xpipe in 'L7JF':
        v1.append(x)
    ypipe = plan[y[0]][y[1]]
    if ypipe in 'L7JF':
        v2.append(y)
    oldx, x = x, loc(oldx, x, xpipe)
    oldy, y = y, loc(oldy, y, ypipe)

vertices = v1 + ([] if plan[x[0]][x[1]] in '-|' else [x]) + v2[::-1]
n = len(vertices)
area = sum(vertices[i][1] * (vertices[(i-1) % n][0] - vertices[(i+1) % n][0]) for i in range(n)) / 2 # Shoelace formula
print((int(abs(area) - i + 1))) # Pick's theorem
