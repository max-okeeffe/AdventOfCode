def main():
    with open("data.txt") as file:
        plan = file.read().split("\n")
        m, n = len(plan), len(plan[0])
        print(sum(valid(plan, m, n, i, j) for i in range(m) for j in range(n)))
    return


def valid(plan, m, n, i, j):
    if plan[i][j] != "@":
        return 0
    
    count = 0
    for x, y in ((i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)):
        if 0 <= x < m and 0 <= y < n and plan[x][y] == "@":
            count += 1
            if count > 3:
                return 0
    return 1


if __name__ == "__main__":
    main()
