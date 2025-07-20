filename = input() + ".txt"
workflow, inputs = list(map(lambda x : x.split('\n'), open(filename).read().split('\n\n')))

rules = {}
for rule in workflow:
    name, conditions = rule.split('{')
    conditions = list(map(lambda x : list(x.split(':')), conditions.strip('}').split(',')))
    conditions[-1].insert(0,'True')
    rules[name] = conditions

def accepted(inp):
    x, m, a, s = tuple(map(lambda x : int(x[2:]), inp.strip('{}').split(',')))
    curr = 'in'
    while True:
        for con, val in rules[curr]:
            if eval(con):
                if val == 'R':
                    return 0
                if val == 'A':
                    return x + m + a + s
                curr = val
                break

print(sum(accepted(inp) for inp in inputs))
