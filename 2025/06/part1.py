import numpy as np


def main():
    with open("data.txt") as file:
        *nums, ops = list(map(lambda x: x.split(), file.read().split("\n")))
        nums = np.array(nums).astype(int)
        print(total(nums, ops))
    return


def total(nums, ops):
    n = len(ops)
    return np.sum(np.sum(nums[:,i]) if ops[i] == "+" else np.prod(nums[:,i]) for i in range(n))


if __name__ == "__main__":
    main()
