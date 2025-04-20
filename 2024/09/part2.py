filename = input() + ".txt"
diskmap = open(filename).read()

expand_map = []
for i in range(len(diskmap)):
    if i % 2:
        expand_map += ['.'] * int(diskmap[i])
    else:
        expand_map += [str(i // 2)] * int(diskmap[i])

N = len(diskmap) // 2
lastnum = len(expand_map) - 1

while N >= 0:
    space = int(diskmap[2 * N])
    if '.' * space in ''.join(expand_map[:lastnum]):
        while expand_map[lastnum] != str(N):
            lastnum -= 1
        while expand_map[lastnum] == str(N):
            lastnum -= 1
        firstdot = 0
        while expand_map[firstdot : firstdot + space] != ['.'] * space:
            firstdot += 1
        expand_map[firstdot : firstdot + space], expand_map[lastnum + 1 : lastnum + space + 1] = [str(N)] * space, ['.'] * space
    N -= 1

print(sum(index * (int(digit) if digit.isnumeric() else 0) for index, digit in enumerate(expand_map)))
