filename = input() + ".txt"
diskmap = open(filename).read()

def expand(map):
    output = []
    for i in range(len(map)):
        if i % 2:
            output += ['.'] * int(map[i])
        else:
            output += [str(i // 2)] * int(map[i])
    return output

def move(file):
    firstdot = 0
    lastnum = len(file)-1

    while lastnum - firstdot > 1:
        while file[firstdot] != '.':
            firstdot += 1
        while file[lastnum] == '.':
            lastnum -= 1
        file[firstdot], file[lastnum] = file[lastnum], file[firstdot]
    return [int(char) for char in file if char != '.']

print(sum(index * digit for index, digit in enumerate(move(expand(diskmap)))))
