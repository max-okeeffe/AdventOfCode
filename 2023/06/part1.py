filename = input() + ".txt"
time, dist = tuple(map(lambda x : tuple(map(int, x.split()[1:])), open(filename).read().split('\n')))
n = len(time)

count = 1
for i in range(n):
    t, d = time[i], dist[i]
    a, b = int( (t - (t ** 2 - 4 * d) ** 0.5) / 2 ), int( (t + (t ** 2 - 4 * d) ** 0.5) / 2 )
    if (t - b) * b == d:
        b -= 1
    count *= b - a

print(count)
