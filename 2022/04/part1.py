filename = input() + ".txt"
assignments = open(filename).read().split('\n')

def overlap(pair):
    pair1, pair2 = pair.split(',')
    a,b = tuple(map(int,pair1.split('-')))
    x,y = tuple(map(int,pair2.split('-')))
    if a <= x and y <= b or x <= a and b <= y:
        return 1
    return 0

print(sum(overlap(pair) for pair in assignments))
