def x(nums):
    first = nums[0]

    print(nums)
    z = []
    while True:
        zz = []
        for i in range(len(nums) - 1):
            zz.append(nums[i + 1] - nums[i])
        z.append(zz)
        if len(list(set(zz))) == 1:
            break
        else:
            nums = zz

    [print(zz) for zz in z]

    if len(z) == 1:
        return first - z[0][0]

    o = 0
    print(f"{o=}")
    for i in range(len(z) - 2, -2, -1):
        print(z[i + 1][0])
        o = z[i + 1][0] - o
        print(f"{o=}")
    return first - o


def main():
    total = 0
    with open("../input.txt") as f:
        for line in f:
            history = list(map(lambda h: int(h), line.strip().split()))
            prediction = x(history)
            print(prediction, history)
            total += prediction
    print(total)


main()
