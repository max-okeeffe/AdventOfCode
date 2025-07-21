from math import prod

filename = input() + ".txt"
workflow, inputs = list(map(lambda x : x.split('\n'), open(filename).read().split('\n\n')))

rules = {}
for e, rule in enumerate(workflow):
    name, conditions = rule.split('{')
    conditions = list(map(lambda x : list(x.split(':')), conditions.strip('}').split(',')))
    conditions[-1].insert(0,'True')
    rules[name] = conditions

todo, count = [[1,4000,1,4000,1,4000,1,4000,'in',0]], 0
while todo:
    *bounds, label, index = todo.pop()
    con, val = rules[label][index]
    x, num = con[0], int(con[2:])
    i = 'xmas'.index(x)
    box1, box2 = [x for x in bounds], [x for x in bounds]

    if con[1] == '<':
        box1[2*i+1], box2[2*i] = num-1, num
    else:
        box1[2*i], box2[2*i+1] = num+1, num

    if val == 'A':
        count += prod(box1[2*i+1] - box1[2*i] + 1 for i in range(4))
    elif val != 'R':
        todo.append(box1 + [val, 0])

    nextcon, nextval = rules[label][index+1]
    if nextcon == 'True':
        if nextval == 'A':
            count += prod(box2[2*i+1] - box2[2*i] + 1 for i in range(4))
        elif nextval != 'R':
            todo.append(box2 + [nextval, 0])
    else:
        todo.append(box2 + [label, index+1])

print(count)
