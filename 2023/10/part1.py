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
if a > 0 and plan[a-1][b] in ['|', '7', 'F']:
    entries.append((a-1,b))
if a < m-1 and plan[a+1][b] in ['|', 'L', 'J']:
    entries.append((a+1,b))
if b > 0 and plan[a][b-1] in ['-', 'F', 'L']:
    entries.append((a,b-1))
if b < n-1 and plan[a][b+1] in ['-', 'J', '7']:
    entries.append((a,b+1))

def loc(oldx, x, pipe):
    a,b = x
    i,j = oldx
    di, dj = a-i, b-j

    if pipe in ['-', '|']:
        return (a+di,b+dj)
    
    if pipe in ['L', '7']:
        return (a+dj,b+di)
    
    return (a-dj,b-di)

x, y = entries
oldx, oldy, i = (a,b), (a,b), 1
while x != y:
    xpipe = plan[x[0]][x[1]]
    ypipe = plan[y[0]][y[1]]
    oldx, x = x, loc(oldx, x, xpipe)
    oldy, y = y, loc(oldy, y, ypipe)
    i += 1

print(i)
