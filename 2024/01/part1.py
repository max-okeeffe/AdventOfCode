filename = input() + '.txt'

pairs, N = [ row.split() for row in open(filename).read().split('\n')], len(open(filename).read().split('\n'))
list1, list2 = sorted([int(item[0]) for item in pairs]), sorted([int(item[1]) for item in pairs])

print(sum(abs(list1[i] - list2[i]) for i in range(N)))
