def main():
    with open("data.txt") as file:
        intervals = map(lambda s: s.split("-"), file.read().split(","))
        print(sum(invalid(interval) for interval in intervals))
    return


def invalid(interval):
    output = 0
    seen = set()
    a, b = interval
    m, n = len(a), len(b)

    for k in range(2, n+1):
        a, b = interval
 
        if m % k:
            x = str(10 ** (m // k))
            a = int(x * k)
        else:
            x = a[: m // k]
            a = int(a)

        if n % k:
            b = 10 ** (n-(n % k)) - 1
        else:
            b = int(b)

        while a > int(x * k):
            x = str(int(x)+1)

        while a <= int(x * k) <= b:
            if int(x * k) not in seen:
                output += int(x * k)
                seen.add(int(x * k))
            x = str(int(x)+1)

    return output


if __name__ == "__main__":
    main()
