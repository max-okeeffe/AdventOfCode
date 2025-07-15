filename = input() + ".txt"
plan = [[x for x in row] for row in open(filename).read().split('\n')]

m, n = len(plan), len(plan[0])

def north():
    load = []
    for i in range(m):
        for j in range(n):
            if plan[i][j] == 'O':
                k = 1
                while i-k >= 0 and plan[i-k][j] == '.':
                    k += 1
                plan[i][j], plan[i-k+1][j] = plan[i-k+1][j], plan[i][j]
                load.append((i-k+1,j))
    return load

def west():
    load = []
    for j in range(n):
        for i in range(m):
            if plan[i][j] == 'O':
                k = 1
                while j-k >= 0 and plan[i][j-k] == '.':
                    k += 1
                plan[i][j], plan[i][j-k+1] = plan[i][j-k+1], plan[i][j]
                load.append((i,j-k+1))
    return load

def south():
    load = []
    for i in range(m-1,-1,-1):
        for j in range(n):
            if plan[i][j] == 'O':
                k = 1
                while i+k < m and plan[i+k][j] == '.':
                    k += 1
                plan[i][j], plan[i+k-1][j] = plan[i+k-1][j], plan[i][j]
                load.append((i+k-1,j))
    return load

def east():
    load = []
    for j in range(n-1,-1,-1):
        for i in range(m):
            if plan[i][j] == 'O':
                k = 1
                while j+k < n and plan[i][j+k] == '.':
                    k += 1
                plan[i][j], plan[i][j+k-1] = plan[i][j+k-1], plan[i][j]
                load.append((i,j+k-1))
    return load

visited, i = [], 0
while True:
    state = []
    for fun in (north, west, south, east):
        state.append(fun())
    if state in visited:
        j = visited.index(state)
        break
    visited.append(state)
    i += 1

for k in range((1000000000 - j) % (i-j) - 1):
    for fun in (north, west, south, east):
        fun()

print(sum(m-i for i in range(m) for j in range(n) if plan[i][j] == 'O'))
