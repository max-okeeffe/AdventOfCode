filename = input() + ".txt"
codes = open(filename).read().split(',')

def hash(str):
    curr = 0
    for x in str:
        curr = ((curr + ord(x)) * 17) % 256
    return curr

boxes = [[] for _ in range(256)]
for code in codes:
    if '=' in code:
        (label, length) = code.split('=')
        n = hash(label)
        box = boxes[n]
        for i in range(len(box)):
            if label in box[i]:
                box[i] = (label, int(length))
                break
        else:
            box.append((label, int(length)))
    else:
        label = code.split('-')[0]
        n = hash(label)
        box = boxes[n]
        for item in box:
            if item[0] == label:
                box.remove(item)
                break

print(sum((i+1) * (j+1) * boxes[i][j][1] for i in range(len(boxes)) for j in range(len(boxes[i]))))
