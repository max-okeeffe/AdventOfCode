from sys import setrecursionlimit

filename = input() + ".txt"
plan = open(filename).read().split('\n')

setrecursionlimit(10000)
m, n = len(plan), len(plan[0])

energised = set()
def light(start, dir):
    if (start, dir) in energised:
        return
    energised.add((start,dir))

    a, b = start
    i, j = dir
    x, y = a+i, b+j

    if x in (-1,m) or y in (-1,n):
        return

    val = plan[x][y]
    if val == '.' or  (val == '-' and i == 0) or (val == '|' and j == 0):
        light((x,y), dir)
        return
    
    if val == '-' and j == 0:
        light((x,y),(0,1))
        light((x,y),(0,-1))
        return
    
    if val == '|' and i == 0:
        light((x,y),(1,0))
        light((x,y),(-1,0))
        return

    if val == '/':
        if j == 1:
            light((x,y),(-1,0))
            return
        if j == -1:
            light((x,y),((1,0)))
            return
        if i == 1:
            light((x,y),(0,-1))
            return
        light((x,y),(0,1))
        return
    
    if j == 1:
        light((x,y),(1,0))
        return
    if j == -1:
        light((x,y),(-1,0))
        return
    if i == 1:
        light((x,y),(0,1))
        return
    light((x,y),(0,-1))
    return

light((0,-1),(0,1))
print(len({x for x, _ in energised if x != (0,-1)}))
