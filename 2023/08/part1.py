filename = input() + ".txt"
steps, nodes = open(filename).read().split('\n\n')
nodes = map(lambda x : x.split(' = '), nodes.split('\n'))

n, d = len(steps), {}
for source, targets in nodes:
    d[source] = targets.strip('()').split(', ')

curr, i = 'AAA', 0
while curr != 'ZZZ':
    curr = d[curr][0 if steps[i % n] == 'L' else 1]
    i += 1

print(i)
