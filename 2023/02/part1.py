filename = input() + ".txt"
games = open(filename).read().split('\n')

def valid(game):
    id, rounds = game.split(': ')
    for round in rounds.split('; '):
        for item in round.split(', '):
            item = item.split(' ')
            num, colour = int(item[0]), item[1]
            if colour == 'blue' and num > 14 or colour == 'green' and num > 13 or colour == 'red' and num > 12:
                return 0
    return int(id.split(' ')[-1])

print(sum(valid(game) for game in games))
