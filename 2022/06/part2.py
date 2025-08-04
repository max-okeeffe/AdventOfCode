filename = input() + ".txt"
s = open(filename).read()

i = 14
while len(set(s[i-14:i])) < 14:
    i += 1

print(i)
