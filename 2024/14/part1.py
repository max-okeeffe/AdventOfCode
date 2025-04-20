import re
filename = input() + ".txt"
robots = [[int(char) for char in re.findall(r'\d+|\-\d+', line)] for line in open(filename).read().split('\n')]

m, n, secs, counts = 101, 103, 100, [0,0,0,0]

for robot in robots:
    x,y,v,w = robot
    a,b = ((x + secs * v) % m) - (m // 2), ((y + secs * w) % n) - (n // 2)
    if a > 0 and b > 0:
        counts[0] += 1
    if a < 0 and b > 0:
        counts[1] += 1
    if a > 0 and b < 0:
        counts[2] += 1
    if a < 0 and b < 0:
        counts[3] += 1

print(counts[0] * counts[1] * counts[2] * counts[3])
