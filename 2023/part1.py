import numpy as np

filename = input() + ".txt"
data = open(filename).read().split('\n')

inits = []
while data:
    inits.append(tuple(map(lambda x : tuple(map(int, x.split(', '))), data.pop().split(' @ '))))
N = len(inits)

def find_non_zero_row(X,i,j):
    for k in range(i+1,len(X)):
        if X[k,j] != 0:
            return k
    return None

def swap_rows(X,i,j):
    X[[i,j]] = X[[j,i]]

def multiply_row(X,i,j):
    val = X[i,j]
    for k in range(len(X[0])):
        X[i,k] = X[i,k] / val

def subtract_row(X,i,j):
    for k in range(len(X)):
        if k != i:
            X[k] -= X[k,j] * X[i]

def rref(X):
    i, j = 0, 0
    m, n = len(X), len(X[0])
    while True:
        if X[i,j]:
            multiply_row(X,i,j)
            subtract_row(X,i,j)
            i += 1
            j += 1
            if i == m or j == n:
                return X
        else:
            k = find_non_zero_row(X,i,j)
            if k is None:
                j += 1
                if j == n:
                    return X
            else:
                swap_rows(X,i,k)

def intersect(init1, init2):
    pos1, vel1 = init1
    pos2, vel2 = init2
    a0, a1, a2 = pos1
    r0, r1, r2 = vel1
    b0, b1, b2 = pos2
    q0, q1, q2 = vel2

    X = rref(np.array([[r0, -q0, b0-a0],[r1,-q1, b1-a1]], dtype = float))
    m, n = len(X), len(X[0])
    x, y = X[0,n-1], X[1,n-1]
    for k in range(n-1):
        if X[m-1,k] != 0:
            break
    else:
        return False
    return x >= 0 and y >= 0 and 200000000000000 <= a0 + x * r0 <= 400000000000000 and 200000000000000 <= a1 + x * r1 <= 400000000000000

print(sum(intersect(inits[i],inits[j]) for i in range(N-1) for j in range(i+1,N)))
