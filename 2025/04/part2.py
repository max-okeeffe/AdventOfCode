from collections import deque

def main():
    with open("data.txt") as file:
        plan = [[x for x in row] for row in file.read().split("\n")]
        m, n = len(plan), len(plan[0])
        count = 0
        Q = deque()

        for i in range(m):
            for j in range(n):
                if plan[i][j] == "@":
                    Q.append((i,j))
                
        while Q:
            i, j = Q.popleft()
            if valid(plan, m, n, i, j):
                count += 1
                for x, y in ((i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)):
                    if 0 <= x < m and 0 <= y < n and plan[x][y] == "@":
                        Q.append((x,y))
                plan[i][j] = "."
        print(count)
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
