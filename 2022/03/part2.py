filename = input() + ".txt"
contents = open(filename).read().split('\n')

priority = {x : i + 1 for i, x in enumerate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')}

def common(i):
    pack1, pack2, pack3 = contents[i:i+3]
    for x in pack1:
        if x in pack2 and x in pack3:
            return priority[x]
        
print(sum(common(3 * i) for i in range(len(contents) // 3)))
