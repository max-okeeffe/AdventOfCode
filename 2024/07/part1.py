filename = input() + ".txt"

puzzles = [row.split() for row in open(filename).read().split('\n')]

def possible(puzzle):
    target, inputs = int(puzzle[0][:-1]), [int(inp) for inp in puzzle[1:]]
    N = len(inputs) - 1
    ops = [bin(n)[2:].zfill(N) for n in range(2**N)]

    for op in ops:
        val = inputs[0]
        for i in range(N):
            val = val + inputs[i+1] if int(op[i]) else val * inputs[i+1]
            if val > target:
                break
        if val == target:
            return target
    return 0

print(sum(possible(puzzle) for puzzle in puzzles))
