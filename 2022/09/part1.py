filename = input() + ".txt"
moves = open(filename).read().split('\n')

H, T = [0,0], [0,0]
visited = {(0,0)}
dir = {'D' : (1,0), 'U' : (-1,0), 'L' : (0,-1), 'R' : (0,1)}

def update(H,T,D):
    
    i,j = dir[D]
    if i:
        H[0] += i
    else:
        H[1] += j

    a,b = H
    c,d = T
    x,y = a-c, b-d

    if abs(x) == 2 or abs(y) == 2:

        if abs(x) == 2:
            T[0] += x // 2
        else:
            T[0] += x
    
        if abs(y) == 2:
            T[1] += y // 2
        else:
            T[1] += y
    
    return tuple(T)
    
for move in moves:
    d, n = move.split()
    for _ in range(int(n)):
        visited.add(update(H,T,d))

print(len(visited))
