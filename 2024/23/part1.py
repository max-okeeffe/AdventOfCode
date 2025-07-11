filename = input() + ".txt"
connections = open(filename).read().split('\n')

vertices, edges = set(), []
for connection in connections:
    x, y = connection.split('-')
    edges.append({x,y})
    vertices.update({x,y})

def triangle(edge, vertex):
    if all(x[0] != 't' for x in edge) and vertex[0] != 't':
        return False
    for node in edge:
        if {vertex, node} not in edges:
            return False
    return True

print(sum(triangle(edge,vertex) for edge in edges for vertex in vertices) // 3)
