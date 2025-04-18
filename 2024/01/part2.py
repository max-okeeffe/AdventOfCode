filename = input() + '.txt'

pairs, N = [ row.split() for row in open(filename).read().split('\n')], len(open(filename).read().split('\n'))
list1, list2 = [int(item[0]) for item in pairs], [int(item[1]) for item in pairs]

print(sum(item * list2.count(item) for item in list1))
