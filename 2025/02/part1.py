def main():
    with open("data.txt") as file:
        intervals = map(lambda s: s.split("-"), file.read().split(","))
        print(sum(invalid(interval) for interval in intervals))
    return


def invalid(interval):
    a, b = interval
    m, n = len(a), len(b)

    if m == n and m % 2:
        return 0
    
    if m % 2:
        x = str(10 ** (m // 2))
        a = 10 ** m + 10 ** (m // 2)
    else:
        x = a[: m // 2]
        a = int(a)

    if n % 2:
        b = 10 ** (n-1) - 1
    else:
        b = int(b)

    while a > int(x+x):
        x = str(int(x)+1)

    output = 0
    while a <= int(x+x) <= b:
        output += int(x+x)
        x = str(int(x)+1)
    return output  


if __name__ == "__main__":
    main()
