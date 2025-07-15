filename = input() + ".txt"
codes = open(filename).read().split(',')

def hash(str):
    curr = 0
    for x in str:
        curr = ((curr + ord(x)) * 17) % 256
    return curr

print(sum(hash(code) for code in codes))
