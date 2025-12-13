from scipy.cluster.hierarchy import DisjointSet


def main():
    with open("data.txt") as file:
        coords = [tuple(map(int, line.strip().split(","))) for line in file]
        print(total(coords))
    return


def d(alpha, beta):
    a, b, c = alpha
    x, y, z = beta
    return (a-x) ** 2 + (b-y) ** 2 + (c-z) ** 2


def total(coords):
    n = len(coords)
    circuits = DisjointSet(coords)
    pairs = sorted([(coords[i], coords[j]) for i in range(n-1) for j in range(i+1, n)], key=lambda x: d(x[0], x[1]))[:1000]
    for a, b in pairs:
        circuits.merge(a, b)
    a, b, c= sorted(list(map(len, circuits.subsets())), reverse=True)[:3]
    return a * b * c


if __name__ == "__main__":
    main()
