filename = input() + ".txt"
rounds = open(filename).read().split('\n')

myscore = {'X' : 1, 'Y' : 2, 'Z' : 3}
opscore = {'A' : 1, 'B' : 2, 'C' : 3}
def roundscore(op,my):
    ops, mys = opscore[op], myscore[my]
    if ops == mys:
        return 3
    if (ops, mys) in ((1,2), (2, 3), (3, 1)):
        return 6
    return 0

def score(round):
    op, my = round.split()
    return myscore[my] + roundscore(op,my)

print(sum(score(round) for round in rounds))
