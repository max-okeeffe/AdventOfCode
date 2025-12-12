def main():
    with open("data.txt") as file:
        ranges, items = file.read().split("\n\n")
        ranges = list(map(lambda x: list(map(int, x.split("-"))), ranges.split("\n")))
        items = map(int, items.split("\n"))
        print(sum(available(ranges, item) for item in items))
    return


def available(ranges, item):
    for x in ranges:
        a, b = x
        if a <= item <= b:
            return 1
    return 0
    

if __name__ == "__main__":
    main()
