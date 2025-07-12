from regex import findall

filename = input() + ".txt"
lines = open(filename).read().split('\n')

pattern = r"([1-9]|one|two|three|four|five|six|seven|eight|nine)"

numeric = {
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9'
}

for x in '123456789':
    numeric[x] = x

def digits(str):
    matches = findall(pattern, str, overlapped = True)
    x, y = numeric[matches[0]], numeric[matches[-1]]
    return int(x + y)

print(sum(digits(line) for line in lines))
