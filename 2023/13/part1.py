filename = input() + ".txt"
plans = map(lambda x : x.split('\n'), open(filename).read().split('\n\n'))

def summ(plan):
    m, n = len(plan), len(plan[0])

    for j in range(n-1):
        j1, j2 = j, j+1
        while 0 <= j1 and j2 < n:
            if any(plan[i][j1] != plan[i][j2] for i in range(m)):
                break
            j1 -= 1
            j2 += 1
        else:
            return j+1
    
    for i in range(m-1):
        i1, i2 = i, i+1
        while 0 <= i1 and i2 < m:
            if any(plan[i1][j] != plan[i2][j] for j in range(n)):
                break
            i1 -= 1
            i2 += 1
        else:
            return 100 * (i+1)
    
print(sum(summ(plan) for plan in plans))
