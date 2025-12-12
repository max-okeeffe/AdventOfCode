import numpy as np


def main():
    with open("data.txt") as file:
        tps = np.transpose(np.array([[x for x in line] for line in file.read().split("\n")]))
        rows = ["".join(row).strip() for row in tps]
        print(total(rows))
    return


def total(rows):
    total = 0
    nums = []
    for row in rows:
        if row:
            try:
                nums.append(int(row))
            except ValueError:
                op = row[-1]
                nums.append(int(row[:-1]))
        else:
            total += np.sum(nums) if op == "+" else np.prod(nums)
            nums = []
    return total + (np.sum(nums) if op == "+" else np.prod(nums))


if __name__ == "__main__":
    main()
