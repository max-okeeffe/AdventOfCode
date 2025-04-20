filename = input() + ".txt"
map = open(filename).read().split('\n')

m, n = len(map[0]), len(map)
zeros = ((i,j) for i in range(m) for j in range(n) if map[j][i] == '0')

def neis(node):
    i, j = node
    return ((nei_i, nei_j) for (nei_i, nei_j) in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)] if 0 <= nei_i < m and 0 <= nei_j < n and int(map[nei_j][nei_i]) == int(map[j][i])+1)

def trailheads(i0):
    return (
        i9
        for i1 in neis(i0)
        for i2 in neis(i1)
        for i3 in neis(i2)
        for i4 in neis(i3)
        for i5 in neis(i4)
        for i6 in neis(i5)
        for i7 in neis(i6)
        for i8 in neis(i7)
        for i9 in neis(i8)
    )
  
print(sum(1 for zero in zeros for nine in trailheads(zero)))
