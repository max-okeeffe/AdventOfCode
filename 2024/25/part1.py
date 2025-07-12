filename = input() + ".txt"
items = open(filename).read().split('\n\n')
locks_keys = ((x.split('\n'), y.split('\n')) for x in items for y in items if x[0] == '#' if y[0] == '.')

def fit(lock, key):
    for j in range(5):
        for i in range(7):
            if lock[i][j] == key[i][j] == '#':
                return 0
    return 1

print(sum(fit(lock, key) for lock, key in locks_keys))
