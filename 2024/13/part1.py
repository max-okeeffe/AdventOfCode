import re
filename = input() + ".txt"
machines = [[int(char) for line in machine.split('\n') for char in re.findall(r'\d+', line)] for machine in open(filename).read().split('\n\n')]

def cost(machine):
    a,c,b,d,x,y = machine
    det = a * d - b * c
    if (d * x - b * y) % det == 0 and (a * y - c * x) % det == 0:
        return 3 * (d * x - b * y) // det + (a * y - c * x) // det
    return 0

print(sum(cost(machine) for machine in machines))
