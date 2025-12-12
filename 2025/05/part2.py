def main():
    with open("data.txt") as file:
        ranges, _ = file.read().split("\n\n")
        ranges = list(map(lambda x: list(map(int, x.split("-"))), ranges.split("\n")))
        print(sum(x[1]-x[0]+1 for x in available(ranges)))
    return


def available(ranges):
    ranges.sort()
    disjoint = []
    for x in ranges:
        a, b = x
        for y in disjoint:
            c, d = y
            if b >= c and a <= d:
                disjoint.append([min(a,c), max(b,d)])
                disjoint.remove(y)
                break
        else:
            disjoint.append([a,b])
    return disjoint
    

if __name__ == "__main__":
    main()
