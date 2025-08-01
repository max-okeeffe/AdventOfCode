filename = input() + ".txt"
rounds = open(filename).read().split('\n')

myscore = {'X' : 0, 'Y' : 3, 'Z' : 6}
opscore = {'A' : 1, 'B' : 2, 'C' : 3}
def roundscore(op,my):
    ops = opscore[op]
    if my == 'Y':
        return ops
    if my == 'Z':
        return 1 if ops == 3 else ops + 1
    return 3 if ops == 1 else ops - 1

def score(round):
    op, my = round.split()
    return myscore[my] + roundscore(op,my)

print(sum(score(round) for round in rounds))
