filename = input() + ".txt"
map = open(filename).read().split('\n')

m, n = len(map), len(map[0])

def valid(i,j,k):
    neis = [
        (nei_i,nei_j)
        for nei_i, nei_j in [(i-1,y) for y in range(j-1,k+1)] + [(i+1,y) for y in range(j-1,k+1)] + [(i,j-1),(i,k)] 
        if 0 <= nei_i < m and 0 <= nei_j < n
    ]
    return any(map[a][b] not in '1234567890.' for a, b in neis)

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
    if valid(*inp):
        count += int(num)

    if i < m and j == n:
        i += 1
        j = 0

    if (i,j) == (m-1,n-1):
        break
    
print(count)
