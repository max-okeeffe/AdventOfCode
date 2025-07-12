filename = input() + ".txt"
games = open(filename).read().split('\n')

def valid(game):
    maxb, maxr, maxg = 0, 0, 0
    _, rounds = game.split(': ')
    for round in rounds.split('; '):
        for item in round.split(', '):
            item = item.split(' ')
            num, colour = int(item[0]), item[1]
            if colour == 'blue' and num > maxb:
                maxb = num
            elif colour == 'green' and num > maxg:
                maxg = num
            elif colour == 'red' and num > maxr:
                maxr = num
    return maxb * maxg * maxr

print(sum(valid(game) for game in games))
