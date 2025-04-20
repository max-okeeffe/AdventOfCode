import re
filename = input() + ".txt"
robots = [[int(char) for char in re.findall(r'\d+|\-\d+', line)] for line in open(filename).read().split('\n')]

m, n, N = 101, 103, len(robots)

for secs in range(1,10000):
    positions = []
    for robot in robots:
        x,y,v,w = robot
        a,b = (x + secs * v) % m, (y + secs * w) % n
        if (a,b) in positions:
            break
        positions.append((a,b))
    if len(positions) == N:
        break

print(secs)
