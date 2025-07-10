filename = input() + ".txt"
codes = open(filename).read().split('\n')

num = {
    '7' : (0,0),
    '8' : (0,1),
    '9' : (0,2),
    '4' : (1,0),
    '5' : (1,1),
    '6' : (1,2),
    '1' : (2,0),
    '2' : (2,1),
    '3' : (2,2),
    '0' : (3,1),
    'A' : (3,2)
}

dir = {
    '^' : (0,1),
    'A' : (0,2),
    '<' : (1,0),
    'v' : (1,1),
    '>' : (1,2)
}

def code_translate(str):
    newstr, n = 'A' + str, len(str)
    paths = ['']
    for k in range(n):
        x, y = newstr[k], newstr[k+1]
        num_x, num_y = num[x], num[y]
        i, j = num_y[0] - num_x[0], num_y[1] - num_x[1]     

        if i == 0:
            str_i = ''
        elif i < 0:
            str_i = '^' * (-i)
        else:
            str_i = 'v' * i

        if j == 0:
            str_j = ''
        elif j < 0:
            str_j = '<' * (-j)
        else:
            str_j = '>' * j

        newpaths = []
        for path in paths:
            if x in '0A' and y in '147':
                newpaths.append(path + str_i + str_j + 'A')
            elif x in '147' and y in '0A':
                newpaths.append(path + str_j + str_i + 'A')
            else:
                for item in {str_i + str_j + 'A', str_j + str_i + 'A'}:
                    newpaths.append(path + item)
        paths = newpaths

    N = min(len(path) for path in paths)
    return (path for path in paths if len(path) == N)

def translate(str):
    newstr, n = 'A' + str, len(str)
    paths = ['']
    for k in range(n):
        x, y = newstr[k], newstr[k+1]
        dir_x, dir_y = dir[x], dir[y]
        i, j = dir_y[0] - dir_x[0], dir_y[1] - dir_x[1]

        if i == 0:
            str_i = ''
        elif i < 0:
            str_i = '^' * (-i)
        else:
            str_i = 'v' * i

        if j == 0:
            str_j = ''
        elif j < 0:
            str_j = '<' * (-j)
        else:
            str_j = '>' * j

        newpaths = []
        for path in paths:
            if x in '^A' and y == '<':
                newpaths.append(path + str_i + str_j + 'A')
            elif x == '<' and y in '^A':
                newpaths.append(path + str_j + str_i + 'A')
            else:
                for item in {str_i + str_j + 'A', str_j + str_i + 'A'}:
                    newpaths.append(path + item)
        paths = newpaths

    N = min(len(path) for path in paths)
    return (path for path in paths if len(path) == N)

d = {}
def com(str, n):
    if (str,n) in d:
        return d[(str,n)]
    
    if n == 0:
        d[(str,n)] = len(str)
        return len(str)
    
    new, newstr = [], ''
    for i in range(len(str)):
        newstr += str[i]
        if str[i] == 'A':
            new.append(newstr)
            newstr = ''

    val = sum( min(com(item, n-1) for item in translate(newstr)) for newstr in new)
    d[(str, n)] = val
    return val

count = 0
for code in codes:
    numcode = int(code[:-1])
    lencode = min(com(x, 2) for x in code_translate(code))
    count += numcode * lencode

print(count)
