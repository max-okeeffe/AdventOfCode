filename = input() + ".txt"
elves = open(filename).read().split('\n\n')

maxval = [0, 0, 0]
for elf in elves:
    val = sum(map(int, elf.split('\n')))
    if val >= maxval[0]:
        maxval[0], maxval[1], maxval[2] = val, maxval[0], maxval[1]
    elif val >= maxval[1]:
        maxval[1], maxval[2] = val, maxval[1]
    elif val >= maxval[2]:
        maxval[2] = val

print(sum(maxval))
