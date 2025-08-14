filename = input() + ".txt"
actions = open(filename).read().split('\n')

total_strength = ''
X = 1
cycle = 0

def check(cycle, X):
    if X <= cycle % 40 <= X+2:
        return '#'
    return '.'

for action in actions:
    if action == 'noop':
        cycle += 1
        total_strength += check(cycle, X)
    else:
        cycle += 1
        total_strength += check(cycle, X)
        cycle += 1
        total_strength += check(cycle, X)
        
        _, n = action.split()
        X += int(n)

for i in range(6):
    print(' '.join(total_strength[40*i:40*(i+1)]))
