filename = input() + ".txt"
moves = open(filename).read().split('\n')

rope = [[0,0] for _ in range(10)]
visited = {(0,0)}
dir = {'D' : (1,0), 'U' : (-1,0), 'L' : (0,-1), 'R' : (0,1)}

def update(rope,D):
    
    i,j = dir[D]
    if i:
        rope[0][0] += i
    else:
        rope[0][1] += j

    for k in range(9):
        H, T = rope[k], rope[k+1]

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
    
    return tuple(rope[-1])
    
for move in moves:
    d, n = move.split()
    for _ in range(int(n)):
        visited.add(update(rope,d))

print(len(visited))
