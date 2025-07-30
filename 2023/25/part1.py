from random import choice
from math import prod

filename = input() + ".txt"
data = open(filename).read().split('\n')

edges, nodes = [], set()
for item in data:
    node1, connections = item.split(': ')
    connections = connections.split()
    nodes.add(node1)
    for node2 in connections:
        edges.append((node1, node2))
        nodes.add(node2)

class Subset:
    def __init__(self,parent,rank):
        self.parent = parent
        self.rank = rank

def find(subsets, node):
    if subsets[node].parent != node:
        subsets[node].parent = find(subsets, subsets[node].parent)
    return subsets[node].parent

def Union(subsets,node1,node2):
    root1 = find(subsets, node1)
    root2 = find(subsets, node2)
    
    if subsets[root1].rank < subsets[root2].rank:
        subsets[root1].parent = root2
    elif subsets[root1].rank > subsets[root2].rank:
        subsets[root2].parent = root1
    else:
        subsets[root2].parent = root1
        subsets[root1].rank += 1

def karger(nodes, edges):
    subsets = {}

    for node in nodes:
        subsets[node] = Subset(node,0)

    N = len(nodes)
    while N > 2:
        edge = choice(edges)
        a, b = edge
        supernode1 = find(subsets, a)
        supernode2 = find(subsets, b)

        if supernode1 == supernode2:
            continue

        N -= 1
        Union(subsets, supernode1, supernode2)

    root = {}
    for node in nodes:
        node_root = find(subsets, node)
        if node_root in root:
            root[node_root] += 1
        else:
            root[node_root] = 1
    
    return prod(root.values())

print(karger(nodes, edges))
