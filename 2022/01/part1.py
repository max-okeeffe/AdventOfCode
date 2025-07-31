filename = input() + ".txt"
elves = open(filename).read().split('\n\n')

maxval = 0
for elf in elves:
    val = sum(map(int, elf.split('\n')))
    if val > maxval:
        maxval = val

print(maxval)
