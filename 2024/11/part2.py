filename = input() + ".txt"
stones = [int(stone) for stone in open(filename).read().split()]

dp = {}
def blink(stone, N):
    if (stone, N) in dp.keys():
        return dp[(stone, N)]

    if N == 1:
        if stone == 0:
            dp[(stone, N)] = 1
            return 1
        elif len(str(stone)) % 2 == 0:
            dp[(stone,N)] = 2
            return 2
        else:
            dp[(stone, N)] = 1
            return 1
        
    if stone == 0:
        val =  blink(1, N-1)
    elif len(str(stone)) % 2 == 0:
        str_stone = str(stone)
        len_stone = len(str_stone) // 2
        val =  blink(int(str_stone[:len_stone]), N-1) + blink(int(str_stone[len_stone:]), N-1)
    else:
        val =  blink(stone * 2024, N-1)

    dp[(stone, N)] = val
    return val

print(sum(blink(stone, 75) for stone in stones))
