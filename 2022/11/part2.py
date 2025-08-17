from collections import deque

filename = input() + ".txt"
monkeys = open(filename).read().split('\n\n')

N = len(monkeys)
counts = [0 for _ in range(N)]
monkey_items = [deque() for _ in range(N)]
operations = []
tests = []
options = []
total = 1

for i, monkey in enumerate(monkeys):
    _, items, operation, test, tcase, fcase = monkey.split('\n')
    for x in list(map(int, items.split(': ')[-1].split(', '))):
        monkey_items[i].append(x)
    operations.append(operation.split('= ')[-1])
    val = int(test.split()[-1])
    tests.append(val)
    total *= val
    options.append([int(tcase.split()[-1]), int(fcase.split()[-1])])

for _ in range(10000):
    for i in range(N):
        op = lambda old : eval(operations[i])
        div = tests[i]
        t, f = options[i]
        while monkey_items[i]:
            counts[i] += 1
            level = op(monkey_items[i].popleft())
            if level % div:
                monkey_items[f].append(level % total)
            else:
                monkey_items[t].append(level % total)
counts.sort()

print(counts[-1] * counts[-2])
