def main():
    with open("data.txt") as file:
        dial = 50
        n = 0
        for line in file:
            dial, n = rotate(dial, line.strip(), n)
        print(n)
    return


def rotate(dial, s, n):
    dir, k = s[0], s[1:]
    k = int(k)
    if dir == "L":
        n += - ((dial - k) // 100)
        return (dial - k) % 100, n
    n += (dial + k) // 100
    return (dial + k) % 100, n


if __name__ == "__main__":
    main()
