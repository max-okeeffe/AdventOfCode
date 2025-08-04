filename = input() + ".txt"
s = open(filename).read()

i = 4
while len(set(s[i-4:i])) < 4:
    i += 1

print(i)
