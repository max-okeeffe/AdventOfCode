filename = input() + ".txt"
plan = map(lambda row : row.split(), open(filename).read().split('\n'))

dir = {'1' : (1,0), '2' : (0,-1), '3' : (-1,0), '0' : (0,1)}
curr, vertices = (0,0), []

i = 0
for item in plan:
    *_, colour = item
    d, n = colour[-2], int(colour[2:-2], 16)
    i += n
    a, b = curr
    x, y = dir[d]
    curr = (a+(n)*x, b+(n)*y)
    vertices.append(curr)

n = len(vertices)
area = int(abs(sum(vertices[i][1] * (vertices[(i-1) % n][0] - vertices[(i+1) % n][0]) for i in range(n))) / 2) # Shoelace formula

print(area + i // 2 + 1) # Overcounting
