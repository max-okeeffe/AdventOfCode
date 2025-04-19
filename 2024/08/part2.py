filename = input() + ".txt"
map = open(filename).read().split('\n')

m, n = len(map[0]), len(map)
N = max(m,n)
coords = [(i,j) for i in range(m) for j in range(n) if map[j][i] != '.']
antennas = []

for x in coords:
    for y in coords:
        if x != y and map[x[1]][x[0]] == map[y[1]][y[0]]:
            for k in range(-N,N+1):
                if 0 <= (1-k) * x[0] + k * y[0] < m and 0 <= (1-k) * x[1] + k * y[1] < n and ((1-k) * x[0] + k * y[0], (1-k) * x[1] + k * y[1]) not in antennas:
                    antennas.append(((1-k) * x[0] + k * y[0], (1-k) * x[1] + k * y[1]))
            
print(len(antennas))
