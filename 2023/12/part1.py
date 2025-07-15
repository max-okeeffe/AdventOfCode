filename = input() + ".txt"
data = list(map(lambda x : x.split(), open(filename).read().split('\n')))

d = {}
def ways(springs, counts):
    
    if (springs, counts) in d:
        return d[(springs, counts)]
    
    if len(counts) == 0:
        if '#' in springs:
            d[(springs, counts)] = 0
            return 0
        return 1
    
    if sum(i+1 for i in counts) - 1 > len(springs):
        d[(springs,counts)] = 0
        return 0
    
    if '?' not in springs:
        groups = [x for x in springs.split('.') if x != '']
        if len(groups) != len(counts):
            d[(springs,counts)] = 0
            return 0
        for i in range(len(groups)):
            if len(groups[i]) != counts[i]:
                d[(springs,counts)] = 0
                return 0
        d[(springs,counts)] = 1
        return 1
    
    a = springs[0]
    if a == '.':
        val = ways(springs[1:], counts)
        d[(springs,counts)] = val
        return val
    
    if a == '?':
        val = ways('.' + springs[1:],counts) + ways('#' + springs[1:], counts)
        d[(springs, counts)] = val
        return val
    
    n = counts[0]
    if any(springs[i] == '.' for i in range(n)):
        d[(springs,counts)] = 0
        return 0
    
    if n < len(springs) and springs[n] == '#':
        d[(springs,counts)] = 0
        return 0
    
    val = ways(springs[n+1:], counts[1:])
    d[(springs, counts)] = val
    return val

count = 0
for x in data:
    springs, counts = x[0], tuple(map(int, x[1].split(',')))
    count += ways(springs,counts)

print(count)
