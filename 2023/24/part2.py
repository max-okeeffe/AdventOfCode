from sympy import solve_poly_system, Symbol

filename = input() + ".txt"
data = open(filename).read().split('\n')

inits = []
while data:
    inits.append(tuple(map(lambda x : tuple(map(int, x.split(', '))), data.pop().split(' @ '))))
N = len(inits)

t, v, p = [], [], []
for i in range(3):
    v.append(Symbol('v' + str(i)))
    p.append(Symbol('p' + str(i)))
    t.append(Symbol('t' + str(i)))

eqns = []
for i in range(3):
    pos, vel = inits[i]
    for j in range(3):
        eqns.append(pos[j] + t[i] * vel[j] - p[j] + t[i] * v[j])

print(sum(solve_poly_system(eqns,*p,*v,*t)[0][:3]))
