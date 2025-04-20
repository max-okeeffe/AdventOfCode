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

def perimeter(region):
    count = 0
    for node in region:
        val = plot[node[1]][node[0]]
        if node[0] in [0,m-1]:
            count += 1
        if node[1] in [0,n-1]:
            count += 1
        for nei in neis(node):
            if plot[nei[1]][nei[0]] != val:
                count += 1
    return count

print(sum(area(region) * perimeter(region) for region in regions))
