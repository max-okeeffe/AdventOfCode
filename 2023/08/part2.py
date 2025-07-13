from math import lcm

filename = input() + ".txt"
steps, nodes = open(filename).read().split('\n\n')
nodes = map(lambda x : x.split(' = '), nodes.split('\n'))

n, d = len(steps), {}
for source, targets in nodes:
    d[source] = targets.strip('()').split(', ')
    
curr, i = tuple(node for node in d.keys() if node[-1] == 'A'), 0
def length(start):
    curr, i = start, 0
    while curr[-1] != 'Z':
        curr = d[curr][0 if steps[i % n] == 'L' else 1]
        i += 1
    return i

# I modified the length function to check if any of the start points hit more than one node ending in 'Z'.
# Since none of them do, it suffices to find the lcm.

print(lcm(*[length(start) for start in curr]))
