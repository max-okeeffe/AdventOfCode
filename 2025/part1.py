def main():
    with open("data.txt") as file:
        print(sum(joltage(bank.strip()) for bank in file))
    return


def joltage(bank):
    left, right = bank[0], bank[1]
    N = len(bank)

    for i in range(1, N-1):
        curr = bank[i]
        if curr > left:
            left = curr
            right = bank[i+1]
        elif curr > right:
            right = curr
    
    if bank[N-1] > right:
        right = bank[N-1]

    return int(left + right)


if __name__ == "__main__":
    main()
