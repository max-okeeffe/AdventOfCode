filename = input() + ".txt"
nums = map(int, open(filename).read().split('\n'))

def f(n):
    n = ((n * 64) ^ n) % 16777216
    n = ((n >> 5) ^ n) % 16777216
    return ((n * 2048) ^ n) % 16777216

changes = {}
for m in nums:
    window, seen = [], []
    n = m
    for _ in range(4):
        n = f(m)
        window.append((n % 10 - m % 10))
        m = n

    for i in range(4, 1999):
        a,b,c,d = window
        if (a,b,c,d) not in seen:
            if (a,b,c,d) in changes:
                changes[(a,b,c,d)] += m % 10
            else:
                changes[(a,b,c,d)] = m % 10
            seen.append((a,b,c,d))

        n = f(m)
        window = [b,c,d,n % 10 - m % 10]
        m = n

print(max(changes.values()))
