filename = input() + ".txt"
data = open(filename).read().split('\n\n')

seeds, *maps = data
seeds = tuple(map(int,seeds.split()[1:]))
conv = lambda x : [tuple(map(int, y.split())) for y in x.split('\n')[1:]]
almanacs = tuple(map(conv,maps))

def findmin(ranges):

    def updateranges(almanac):
        todo, converted = [x for x in ranges], []

        while todo:
            a,b = todo.pop()
            for x,c,d in almanac:
                if a+b > c and c+d > a:
                    if c <= a and a+b <= c+d:
                        converted.append((a+x-c,b))
                    elif a < c and a+b <= c+d:
                        todo.append((a,c-a))
                        converted.append((x,a+b-c))
                    elif c <= a and c+d < a+b:
                        todo.append((c+d,a+b-c-d))
                        converted.append((a+x-c,c+d-a))
                    else:
                        todo.append((a,c-a))
                        todo.append((c+d,a+b-c-d))
                        converted.append((x,d))
                    break
            else:
                converted.append((a,b))

        return converted
    
    for almanac in almanacs:
        ranges = updateranges(almanac)

    return min(a for a, _ in ranges)

ranges = [(seeds[i], seeds[i+1]) for i in range(0,len(seeds),2)]
print(findmin(ranges))
