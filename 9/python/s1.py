

def x(nums):
    last = nums[-1]

    z = []
    while True:
        zz = []
        for i in range(len(nums)-1):
            zz.append(nums[i+1] - nums[i])
        z.append(zz)
        last += zz[-1]
        if len(list(set(zz))) == 1:
            break
        else:
            nums = zz

    return last


def main():
    total = 0
    with open("../input.txt") as f:
        for line in f:
            history = list(map(lambda h: int(h), line.strip().split()))
            total += x(history)
    print(total)

main()