filename = input() + ".txt"
lines = open(filename).read().split('\n')

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.children = []
        self.parent = parent
        self.size = 0

dirs = []
root = Directory('root', None)
outermost = Directory('/', root)
curr_dir = root
curr_dir.children.append(outermost)
dirs.append(outermost)

for line in lines:
    data = line.split()
    if data[0] == '$':
        if data[1] == 'cd':
            if data[2] == '..':
                curr_dir = curr_dir.parent
            else:
                for child in curr_dir.children:
                    if child.name == data[2]:
                        curr_dir = child
                        break
    else:
        if data[0] == 'dir':
            dir = Directory(data[1], curr_dir)
            curr_dir.children.append(dir)
            dirs.append(dir)
        else:
            size = int(data[0])
            new_curr = curr_dir
            while new_curr.parent:
                new_curr.size += size
                new_curr = new_curr.parent

used_space = outermost.size
minsize = used_space
for dir in dirs:
    if dir.size > 30000000 - 70000000 + used_space and dir.size < minsize:
        minsize = dir.size

print(minsize)
