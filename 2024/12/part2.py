filename = input() + ".txt"
plot = open(filename).read().split('\n')

m, n = len(plot[0]), len(plot)
nodes = [(i,j) for i in range(m) for j in range(n)]

class DisjointSet:
    def __init__(self, nodes):
        self.nodes = nodes
        self.parent = {}
        self.size = {}
        for node in nodes:
            self.disjoint_set(node)

    def disjoint_set(self, node):
        self.parent[node] = node
        self.size[node] = 1

    def find(self, node):
        if self.parent[node] == node:
            return node
        else:
            self.parent[node] = self.find(self.parent[node])
            return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2:
            return
        elif self.size[root1] < self.size[root2]:
            self.parent[root1] = root2
            self.size[root2] += self.size[root1]
        else:
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]

garden = DisjointSet(nodes)

def neis(node):
    i,j = node
    return [(nei_i, nei_j) for nei_i, nei_j in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)] if 0 <= nei_i < m and 0 <= nei_j < n]

def outcorner(node):
    i,j = node
    val = plot[j][i]
    count = 0
    for neis in [((i+1,j), (i,j+1)), ((i+1,j), (i,j-1)), ((i-1,j), (i,j+1)), ((i-1,j), (i,j-1))]:
        nei1, nei2 = neis
        if (nei1[0] in [-1,m] or nei1[1] in [-1,n] or plot[nei1[1]][nei1[0]] != val) and (nei2[0] in [-1,m] or nei2[1] in [-1,n] or plot[nei2[1]][nei2[0]] != val):
            #print(nei1[0] in [-1,m], nei1[1] in [-1,n], plot[nei1[1]][nei1[0]] != val, '\n', nei2[0] in [-1,m], nei2[1] in [-1,n], plot[nei2[1]][nei2[0]] != val)
            count += 1
    return count

def incorner(node):
    i,j = node
    val = plot[j][i]
    count = 0
    for neis in [((i+1,j), (i+1,j+1), (i,j+1)), ((i+1,j), (i+1,j-1), (i,j-1)), ((i-1,j), (i-1,j+1), (i,j+1)), ((i-1,j), (i-1,j-1), (i,j-1))]:
        nei1,nei2,nei3 = neis
        if 0 <= nei1[0] < m and 0 <= nei1[1] < n and 0 <= nei2[0] < m and 0 <= nei2[1] < n and 0 <= nei3[0] < m and 0 <= nei3[1] < n and plot[nei1[1]][nei1[0]] == plot[nei3[1]][nei3[0]] == val and plot[nei2[1]][nei2[0]] != val:
            count += 1
    return count

for node in nodes:
    val = plot[node[1]][node[0]]
    for nei in neis(node):
        if plot[nei[1]][nei[0]] == val:
            garden.union(node, nei)

regions = []
for node in nodes:
    if all(node not in region for region in regions):
        regions.append([node1 for node1 in nodes if garden.find(node1) == garden.find(node)])

def area(region):
    return len(region)

def sides(region):
    return sum(outcorner(node) + incorner(node) for node in region)

print(sum(area(region) * sides(region) for region in regions))
