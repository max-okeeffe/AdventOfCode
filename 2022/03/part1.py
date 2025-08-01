filename = input() + ".txt"
contents = open(filename).read().split('\n')

priority = {x : i + 1 for i, x in enumerate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')}

def common(content):
    N = len(content)
    pack1, pack2 = content[:N//2], content[N//2:]
    for x in pack1:
        if x in pack2:
            return priority[x]
        
print(sum(common(content) for content in contents))
