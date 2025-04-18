import re

filename = input() + '.txt'
mystring = open(filename).read()

matches = re.findall("mul\(\d+,\d+\)", mystring)
print(sum( int(match.split(',')[0][4:]) * int(match.split(',')[1][:-1]) for match in matches ))
