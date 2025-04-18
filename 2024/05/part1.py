filename = input() + ".txt"

data = open(filename).read().split('\n\n')
rules, updates = [row.split('|') for row in data[0].split('\n')], [row.split(',') for row in data[1].split('\n')]

def valid(update):
    n = len(update)
    return not any([update[j], update[i]] in rules for i in range(n-1) for j in range(i+1,n))

print(sum(int(update[len(update) // 2]) for update in updates if valid(update)))
