filename = input() + ".txt"
plan = open(filename).read().split('\n')

m, n = len(plan), len(plan[0])

def visible(i,j):
    if i in (0,m) or j in (0,n):
        return 1
    
    if all(plan[k][j] < plan[i][j] for k in range(i)):
        return 1
    
    if all(plan[k][j] < plan[i][j] for k in range(i+1,m)):
        return 1
    
    if all(plan[i][k] < plan[i][j] for k in range(j)):
        return 1
    
    if all(plan[i][k] < plan[i][j] for k in range(j+1,n)):
        return 1

    return 0

print(sum(visible(i,j) for i in range(m) for j in range(n)))
