def main():
    with open("data.txt") as file:
        grid = file.readlines()
        print(total(grid))
    return


def total(grid):
    beams = set()
    total = 0

    i = 0
    while grid[0][i] != "S":
        i += 1
    beams.add(i)

    for line in grid:
        for i, c in enumerate(line):
            if c == "^" and i in beams:
                total += 1
                beams.discard(i)
                beams.add(i-1)
                beams.add(i+1)

    return total
                

if __name__ == "__main__":
    main()
