filename = input() + ".txt"
crates, moves = open(filename).read().split('\n\n')

crates = crates.split('\n')[::-1]
N = max(map(int,crates[0].split()))

stacks = {i : [] for i in range(N)}
for crate in crates[1:]:
    for i, x in enumerate(crate):
        if x not in '[] ':
            stacks[(i-1) // 4].append(x)

moves = moves.split('\n')
for move in moves:
    n, a, b = tuple(map(int,tuple(filter(lambda s : s.isnumeric(), move.split()))))
    for _ in range(n):
        stacks[b-1].append(stacks[a-1].pop())

print(''.join(stacks[x][-1] for x in range(N)))
