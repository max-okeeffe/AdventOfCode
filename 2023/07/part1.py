filename = input() + ".txt"
data = list(map(lambda y : (y[0], int(y[1])), map( lambda x : tuple(x.split()), open(filename).read().split('\n'))))

bids = dict(data)
hands = list(bids.keys())

HIGH, ONE, TWO, THREE, FULL, FOUR, FIVE = 1, 2, 3, 4, 5, 6, 7
score = dict([(str(i),i) for i in range(2,10)] + [('T',10), ('J',11), ('Q',12), ('K',13), ('A',14)])

def type(hand):
    N = len(set(hand))
    scores = tuple(score[x] for x in hand)
    if N == 1:
        return (FIVE,scores)
    
    if N == 4:
        return (ONE,scores)

    if N == 5:
        return (HIGH, scores)
    
    if N == 2:
        if hand.count(hand[0]) in (1, 4):
            return (FOUR, scores)
        return (FULL, scores)
    
    if any(hand.count(x) == 3 for x in hand):
        return (THREE, scores)
    return (TWO, scores)

print(sum(bids[hand] * (i+1) for i, hand in enumerate(sorted(hands, key = type))))
