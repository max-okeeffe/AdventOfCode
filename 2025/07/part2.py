def main():
    with open("data.txt") as file:
        grid = file.readlines()
        print(total(grid))
    return


def total(grid):
    n = len(grid[0])
    beams = set()
    paths = {i: 0 for i in range(-1, n+1)}

    i = 0
    while grid[0][i] != "S":
        i += 1
    beams.add(i)
    paths[i] = 1

    for line in grid:
        for i, c in enumerate(line):
            if c == "^" and i in beams:
                beams.discard(i)
                beams.add(i-1)
                beams.add(i+1)
                paths[i-1] += paths[i]
                paths[i+1] += paths[i]
                paths[i] = 0

    return sum(paths[i] for i in range(n))
                

if __name__ == "__main__":
    main()
