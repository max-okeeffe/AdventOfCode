#filename = input() + ".txt"
filename = "data.txt"
map = open(filename).read().split('\n')

m, n = len(map), len(map[0])

part = {}
def valid(i,j,k):
    neis = [
        (nei_i,nei_j)
        for nei_i, nei_j in [(i-1,y) for y in range(j-1,k+1)] + [(i+1,y) for y in range(j-1,k+1)] + [(i,j-1),(i,k)] 
        if 0 <= nei_i < m and 0 <= nei_j < n
    ]
    for a, b in neis:
        if map[a][b] == '*':
            return (a,b)
    return None

i, j, count = 0, 0, 0
while True:
    while map[i][j] not in '1234567890':
        j += 1
        if j == n:
            i += 1
            j = 0

        if (i,j) == (m-1,n-1):
            break

    num, inp = '', [i,j]
    while j < n and map[i][j] in '1234567890':
        num += map[i][j]
        j += 1

    inp.append(j)
    gear = valid(*inp)
    if gear is not None:
        if gear in part:
            part[gear].append(int(num))
        else:
            part[gear] = [int(num)]

    if i < m and j == n:
        i += 1
        j = 0

    if (i,j) == (m-1,n-1):
        break
    
print(sum(x[0] * x[1] for x in part.values() if len(x) == 2))
