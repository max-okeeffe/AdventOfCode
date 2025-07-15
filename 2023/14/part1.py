filename = input() + ".txt"
plan = [[x for x in row] for row in open(filename).read().split('\n')]

m, n = len(plan), len(plan[0])
for i in range(m):
    for j in range(n):
        if plan[i][j] == 'O':
            k = 1
            while i-k >= 0 and plan[i-k][j] == '.':
                k += 1
            plan[i][j], plan[i-k+1][j] = plan[i-k+1][j], plan[i][j]

print(sum(m-i for i in range(m) for j in range(n) if plan[i][j] == 'O'))
