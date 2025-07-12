filename = input() + ".txt"
connections = open(filename).read().split('\n')

vertices, edges = set(), []
for connection in connections:
    x, y = connection.split('-')
    edges.append({x,y})
    vertices.update({x,y})

neis = {}
for vertex in vertices:
    neis[vertex] = set()

for edge in edges:
    x, y = list(edge)
    neis[x].add(y)
    neis[y].add(x)

maxcycle = [set()]
def BronKerbosch(R,P,X):
    if len(P) == len(X) == 0:
        if len(R) > len(maxcycle[0]):
            maxcycle.pop()
            maxcycle.append(R)
        return
    u = list(P.union(X))[0]
    for v in P - neis[u]:
        BronKerbosch(R.union({v}), P.intersection(neis[v]), X.intersection(neis[v]))
        P = P - {v}
        X = X.union({v})
    return maxcycle

print(','.join(sorted(list(BronKerbosch(set(), vertices, set())[0]))))
