filename = input() + ".txt"
actions = open(filename).read().split('\n')

total_strength = 0
X = 1
cycle = 0

def check(cycle, X):
    if cycle in (20,60,100,140,180,220):
        return X * cycle
    return 0

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

print(total_strength)



    
