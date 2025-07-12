filename = input() + ".txt"
cards = open(filename).read().split('\n')

def points(card):
    wins, guesses = list(map(lambda x : x.split(), card.split(' | ')))
    return sum(1 for x in wins if x in guesses)

counttotals = [1 for _ in range(len(cards))]
for i in range(len(cards)):
    for j in range(i + 1, i + 1 + points(cards[i])):
        counttotals[j] += counttotals[i]

print(sum(counttotals))
