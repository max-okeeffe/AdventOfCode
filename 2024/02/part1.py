filename = input() + '.txt'
rows = [ [int(item) for item in row.split()] for row in open(filename).read().split('\n')]

def increasing(row):
    return all(row[i] < row[i+1] for i in range(len(row)-1))

def decreasing(row):
    return all(row[i] > row[i+1] for i in range(len(row)-1))

def smooth(row):
    return all(abs(row[i] - row[i+1]) <= 3 for i in range(len(row)-1))

def safe(row):
    return (increasing(row) or decreasing(row)) and smooth(row)

print(sum(safe(row) for row in rows))
