from z3 import *

filename = input() + ".txt"
initial, gates = open(filename).read().split('\n\n')
initial, gates = initial.split('\n'), gates.split('\n')

set_param("parallel.enable", True)
s = Tactic("pqffd").solver()

initial = dict(map(lambda x : x.split(':'), initial))
gates = map(lambda x : [x.split(' ')[i] for i in [0,1,2,4]], gates)

variables = {}
for val in initial:
    variables[val] = Int(val)
    s += (variables[val] == initial[val])

for a, fun, b, c in gates:
    for x in (a,b,c):
        if x not in variables:
            variables[x] = Int(x)
            s += Or(variables[x] == 0, variables[x] == 1)
    if fun == 'AND':
        s += (variables[c] == variables[a] * variables[b])
    elif fun == 'OR':
        s += Implies(And(variables[a] == 0, variables[b] == 0), variables[c] == 0)
        s += Implies(Or(variables[a] == 1, variables[b] == 1), variables[c] == 1)
    else:
        s += (variables[c] == (variables[a] + variables[b]) % 2)

if s.check() == sat:
    m = s.model()
    evalu = lambda x:m.evaluate(x).as_long()
    zs = sorted([var for var in variables if var[0] == 'z'])
    print(sum(evalu(variables[x]) * 2 ** i for i, x in enumerate(zs)))
else:
    print("No solution.")
