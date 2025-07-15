filename = input() + ".txt"
plan = open(filename).read().split('\n')

m, n = len(plan), len(plan[0])
cols = [j for j in range(n) if all(plan[i][j] == '.' for i in range(m))]
rows = [i for i in range(m) if all(plan[i][j] == '.' for j in range(n))]

galaxies = [(i,j) for i in range(m) for j in range(n) if plan[i][j] == '#']
N = len(galaxies)

count = 0
for i in range(N-1):
    for j in range(i+1, N):
        a, b = galaxies[i]
        x, y = galaxies[j]
        count += abs(a-x) + abs(b-y) + sum(1 for row in rows if a <= row <= x or x <= row <= a) + sum(1 for col in cols if b <= col <= y or y <= col <= b)

print(count)
