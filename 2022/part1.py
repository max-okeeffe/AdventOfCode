filename = input() + ".txt"
monkeys = open(filename).read().split('\n\n')

monkey_items = []
operations = []
tests = []
options = []

for monkey in monkeys:
    _, items, operation, test, tcase, fcase = monkey.split('\n')
    monkey_items.append(list(map(int, items.split(': ')[-1].split(', '))))
    #op = lambda old : eval(operation.split('= ')[-1])
    operations.append(operation.split('= ')[-1])
    tests.append(int(test.split()[-1]))
    options.append([int(tcase.split()[-1]), int(fcase.split()[-1])])

N = len(monkeys)
counts = [0 for _ in range(N)]

for _ in range(20):
    for i in range(N):
        op = lambda old : eval(operations[i])
        div = tests[i]
        t, f = options[i]
        while monkey_items[i]:
            counts[i] += 1
            level = op(monkey_items[i].pop(0)) // 3
            if level % div:
                monkey_items[f].append(level)
            else:
                monkey_items[t].append(level)
counts.sort()

print(counts[-1] * counts[-2])
