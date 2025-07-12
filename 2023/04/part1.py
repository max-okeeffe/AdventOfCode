filename = input() + ".txt"
cards = open(filename).read().split('\n')

def points(card):
    wins, guesses = list(map(lambda x : x.split(), card.split(' | ')))
    n = sum(1 for x in wins if x in guesses)
    return int(2 ** (n-1))

print(sum(points(card) for card in cards))
