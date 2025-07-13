filename = input() + ".txt"
t, d = tuple(map(lambda x : int(''.join(x.split()[1:])), open(filename).read().split('\n')))

a, b = int( (t - (t ** 2 - 4 * d) ** 0.5) / 2 ), int( (t + (t ** 2 - 4 * d) ** 0.5) / 2 )
if (t - b) * b == d:
    b -= 1
    
print(b-a)
