def main():
    with open("data.txt") as file:
        dial = 50
        n = 0
        for line in file:
            dial = rotate(dial, line.strip())
            if dial == 0:
                n += 1
        print(n)
    return


def rotate(dial, s):
    dir, k = s[0], s[1:]
    if dir == "L":
        return (dial - int(k)) % 100
    return (dial + int(k)) % 100


if __name__ == "__main__":
    main()
