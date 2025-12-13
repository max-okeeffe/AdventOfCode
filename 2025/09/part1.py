def main():
    with open("data.txt") as file:
        corners = list(map(lambda x: tuple(map(int, x.split(","))), file.read().split("\n")))
        print(largest_rectangle(corners))
    return


def d(alpha, beta):
    a, b = alpha
    x, y = beta
    return (abs(a-x)+1) * (abs(b-y)+1)


def largest_rectangle(corners):
    n = len(corners)
    pairs = [d(corners[i], corners[j]) for i in range(n-1) for j in range(i+1, n)]
    return max(pairs)


if __name__ == "__main__":
    main()
