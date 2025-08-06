filename = input() + ".txt"
lines = open(filename).read().split('\n')

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.children = []
        self.parent = parent
        self.size = 0

dirs = []
curr_dir = Directory('root', None)
curr_dir.children.append(Directory('/', curr_dir))
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
            curr_dir.size += int(data[0])

for dir in dirs:
    if not dir.children:
        curr_dir = dir
        while curr_dir.parent:
            curr_dir.parent.size += curr_dir.size
            curr_dir = curr_dir.parent

print(sum(dir.size for dir in dirs if dir.size <= 100000))
