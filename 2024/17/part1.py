import numpy as np

filename = input() + ".txt"
registers, program = open(filename).read().split('\n\n')

program = list(map(int, filter(lambda x : x in '1234567890', program)))
A, B, C = registers.split('\n')
A, B, C = int(A.split()[-1]), int(B.split()[-1]), int(C.split()[-1])

def combo(i):
    if i == 4:
        return A

    if i == 5:
        return B
    
    if i == 6:
        return C
    
    return i

i = 0
output = []

while i < len(program):
    op = program[i]
    lit = program[i+1]
    com = combo(lit)

    if op == 0:
        A //= (2 ** com)

    elif op == 1:
        B ^= lit

    elif op == 2:
        B = com % 8

    elif op == 3:
        if A != 0:
            i = lit - 2

    elif op == 4:
        B ^= C

    elif op == 5:
        output.append(com % 8)

    elif op == 6:
        B = A // (2 ** com)

    else:
        C = A // (2 ** com)

    i += 2

print(','.join(str(x) for x in output))
