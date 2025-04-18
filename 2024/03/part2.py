import re

filename = input() + ".txt"
mystring = open(filename).read()

matches = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", mystring)
val = 1
count = 0

for match in matches:
    if match == "do()":
        val = 1
    elif match == "don't()":
        val = 0
    elif val:
        count += int(match.split(',')[0][4:]) * int(match.split(',')[1][:-1])

print(count)
