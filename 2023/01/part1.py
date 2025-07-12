filename = input() + ".txt"
lines = open(filename).read().split('\n')

def digits(str):
    i, j = 0, -1
    while str[i] not in '1234567890':
        i += 1
    while str[j] not in '1234567890':
        j -= 1
    return int(str[i] + str[j])

print(sum(digits(line) for line in lines))
