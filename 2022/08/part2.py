from math import prod

filename = input() + ".txt"
plan = open(filename).read().split('\n')

m, n = len(plan), len(plan[0])

def dir(i,j,d):
    if d == 0:
        for k in range(1,i+1):
            if plan[i-k][j] >= plan[i][j]:
                return k
        return i
            
    if d == 1:
        for k in range(1,j+1):
            if plan[i][j-k] >= plan[i][j]:
                return k
        return j
            
    if d == 2:
        for k in range(1,m-i):
            if plan[i+k][j] >= plan[i][j]:
                return k
        return m-i-1
            
    if d == 3:
        for k in range(1,n-j):
            if plan[i][j+k] >= plan[i][j]:
                return k
        return n-j-1

def scenic(i,j):
    return prod(dir(i,j,d) for d in range(4))

print(max(scenic(i,j) for i in range(1,m-1) for j in range(1,n-1)))
