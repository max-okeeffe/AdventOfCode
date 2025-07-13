from math import prod

filename = input() + ".txt"
sequences = map(lambda x : tuple(map(int,x.split())), open(filename).read().split('\n'))

def nextstep(seq):
    n = len(seq)
    return sum(seq[j] * prod(-1-i for i in range(n) if i != j) // prod(j-i for i in range(n) if i != j) for j in range(n))

print(sum(nextstep(seq) for seq in sequences))
