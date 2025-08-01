filename = input() + ".txt"
assignments = open(filename).read().split('\n')

def overlap(pair):
    pair1, pair2 = pair.split(',')
    a,b = tuple(map(int,pair1.split('-')))
    x,y = tuple(map(int,pair2.split('-')))
    if b < x or y < a:
        return 0
    return 1

print(sum(overlap(pair) for pair in assignments))
