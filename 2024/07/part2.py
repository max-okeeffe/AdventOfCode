filename = input() + ".txt"
puzzles = [row.split() for row in open(filename).read().split('\n')]

def ternary(n):
    if n == 0:
        return '0'
    digits = ''
    while n:
        digits = str(n % 3) + digits
        n //= 3
    return digits

def possible(puzzle):
    target, inputs = int(puzzle[0][:-1]), [int(inp) for inp in puzzle[1:]]
    N = len(inputs) - 1
    ops = [ternary(n).zfill(N) for n in range(3**N)]

    for op in ops:
        val = inputs[0]
        for i in range(N):
          
            if op[i] == '0':
                val += inputs[i+1]
            elif op[i] == '1':
                val *= inputs[i+1]
            else:
                val = int(str(val) + str(inputs[i+1]))
              
            if val > target:
                break
        if val == target:
            return target
    return 0

print(sum(possible(puzzle) for puzzle in puzzles))
