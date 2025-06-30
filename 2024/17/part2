import numpy as np

filename = input() + ".txt"
registers, program = open(filename).read().split('\n\n')

program = ''.join(filter(lambda x : x in '1234567890', program))

def f(A):
    output = []
    while A > 0:
        B = (A % 8) ^ 7
        C = A >> B
        output.append((B ^ C ^ 7) % 8)
        A = A >> 3
    return ''.join(str(x) for x in output)

potentials = [0]
for i in range(1,len(program)+1):
    temp = []
    for x in potentials:
        n = 8 * x
        for j in range(8):
            if f(n+j)[-i:] == program[-i:]:
                temp.append(n+j)
    potentials = temp

print(min(potentials))

