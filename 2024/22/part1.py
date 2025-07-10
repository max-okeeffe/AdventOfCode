from functools import reduce

filename = input() + ".txt"
nums = map(int, open(filename).read().split('\n'))

def com(f,g):
    return g(f)

def f(n):
    n = ((n * 64) ^ n) % 16777216
    n = ((n >> 5) ^ n) % 16777216
    return ((n * 2048) ^ n) % 16777216

def secret(n):
    return reduce(com, [n, *[f]*2000])

print(sum(secret(n) for n in nums))
