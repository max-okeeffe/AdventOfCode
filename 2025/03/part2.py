def main():
    with open("data.txt") as file:
        print(sum(joltage(bank.strip()) for bank in file))
    return


def joltage(bank):
    vals = [bank[i] for i in range(12)]
    indices = list(range(12))
    N = len(bank)

    for i in range(1, N):
        for j in range(max(0, i-N+12), min(12, i)):
            if bank[i] > vals[j] and i > indices[j]:
                vals[j:] = bank[i:i-j+12]
                indices[j:] = list(range(i,i-j+12))
                break

    return int("".join(vals))


if __name__ == "__main__":
    main()
