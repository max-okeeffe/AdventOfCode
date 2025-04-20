import sys
sys.set_int_max_str_digits(10000)

filename = input() + ".txt"
stones = [int(stone) for stone in open(filename).read().split()]

def blink(stones):
    newstones = []
    for stone in stones:
        if stone == 0:
            newstones.append(1)
        elif len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            len_stone = len(str_stone) // 2
            newstones.append(int(str_stone[:len_stone]))
            newstones.append(int(str_stone[len_stone:]))
        else:
            newstones.append(stone * 2024)
    return newstones

for i in range(25):
    stones = blink(stones)
  
print(len(stones))
