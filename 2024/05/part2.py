filename = input() + ".txt"

data = open(filename).read().split('\n\n')
rules, updates = [row.split('|') for row in data[0].split('\n')], [row.split(',') for row in data[1].split('\n')]

def invalid(update):
    n = len(update)
    return any([update[j], update[i]] in rules for i in range(n-1) for j in range(i+1,n))

count = 0
for update in updates:
    if invalid(update):
        n = len(update)
        for i in range(n-1):
            for j in range(i+1,n):
                if [update[j], update[i]] in rules:
                    update[j], update[i] = update[i], update[j]
        count += int(update[len(update) // 2])

print(count)
