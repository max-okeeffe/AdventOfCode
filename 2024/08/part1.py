filename = input() + ".txt"
map = open(filename).read().split('\n')

m = len(map[0])
n = len(map)
coords = [(i,j) for i in range(m) for j in range(n) if map[j][i] != '.']
antennas = []

for x in coords:
    for y in coords:
        if x != y and map[x[1]][x[0]] == map[y[1]][y[0]]:
            if 0 <= 2 * x[0] - y[0] < m and 0 <= 2 * x[1] - y[1] < n and (2 * x[0] - y[0], 2 * x[1] - y[1]) not in antennas:
                antennas.append((2 * x[0] - y[0], 2 * x[1] - y[1]))
            if 0 <= 2 * y[0] - x[0] < m and 0 <= 2 * y[1] - x[1] < n and (2 * y[0] - x[0], 2 * y[1] - x[1]) not in antennas:
                antennas.append((2 * y[0] - x[0], 2 * y[1] - x[1]))
            
print(len(antennas))
