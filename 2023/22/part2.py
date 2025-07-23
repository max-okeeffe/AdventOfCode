from collections import deque

filename = input() + ".txt"
ends = map(lambda x : tuple(map(lambda y : tuple(map(int, y.split(','))), x.split('~'))), open(filename).read().split('\n'))

class Point:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]

class Brick:
    def __init__(self, name, pos1, pos2):
        self.name = name
        self.pos1 = pos1
        self.pos2 = pos2
        self.supporting = set()
        self.supported = set()

    def drop(self, val):
        self.pos1 = Point((self.pos1.x, self.pos1.y, self.pos1.z - val))
        self.pos2 = Point((self.pos2.x, self.pos2.y, self.pos2.z - val))

    def bottom(self):
        return min(self.pos1.z, self.pos2.z)
    
    def top(self):
        return max(self.pos1.z, self.pos2.z)

    def __str__(self):
        return f"Brick(({self.pos1.x}, {self.pos1.y}, {self.pos1.z}), ({self.pos2.x}, {self.pos2.y}, {self.pos2.z}))"

i, bricks = 1, []
for pos in ends:
    pos1, pos2  = Point(pos[0]), Point(pos[1])
    bricks.append(Brick(i,pos1,pos2))
    i += 1

def above(brick1, brick2):
    if brick1.bottom() <= brick2.top():
        return False
    
    minx1, miny1 = min(brick1.pos1.x, brick1.pos2.x), min(brick1.pos1.y, brick1.pos2.y)
    minx2, miny2 = min(brick2.pos1.x, brick2.pos2.x), min(brick2.pos1.y, brick2.pos2.y)
    maxx1, maxy1 = max(brick1.pos1.x, brick1.pos2.x), max(brick1.pos1.y, brick1.pos2.y)
    maxx2, maxy2 = max(brick2.pos1.x, brick2.pos2.x), max(brick2.pos1.y, brick2.pos2.y)

    if maxx1 >= minx2 and maxx2 >= minx1 and maxy1 >= miny2 and maxy2 >= miny1:
        return True
    return False

bricks.sort(key = lambda brick : brick.bottom())

for brick in bricks:
    if brick.bottom() == 1:
        continue

    lower = [other for other in bricks if other.bottom() < brick.bottom()]

    if not lower:
        brick.drop(brick.bottom() - 1)
        continue

    maxheight = 1
    for other in lower:
        if above(brick, other):
            maxheight = max(maxheight, other.top() + 1)

    brick.drop(brick.bottom() - maxheight)

for brick in bricks:
    for other in bricks:
        if above(brick, other) and other.top() + 1 == brick.bottom():
            other.supporting.add(brick)
            brick.supported.add(other)

def possible(brick):
    if not brick.supporting:
        return 0
    
    Q, d, count = deque(), {}, 0
    Q.append(brick)
    while Q:
        root = Q.popleft()
        for other in root.supporting:
            if other in d:
                d[other] += 1
            else:
                d[other] = 1
            
            if d[other] == len(other.supported):
                count += 1
                Q.append(other)

    return count

print(sum(possible(brick) for brick in bricks))
