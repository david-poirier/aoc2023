def star1():
    with open("../input.txt") as f:
        times = list(map(lambda t: int(t), f.readline().strip().split()[1:]))
        distances = list(map(lambda t: int(t), f.readline().strip().split()[1:]))

        print(times)
        print(distances)

        total = 0

        for i in range(len(times)):
            t = times[i]
            record = distances[i]

            print(t, record)

            winners = 0
            for speed in range(1, t):
                distance = (t - speed) * speed
                if distance > record:
                    winners += 1

            if total == 0:
                total = winners
            else:
                total *= winners

            print(winners, total)


def star2():
    with open("../input.txt") as f:
        time = int(f.readline().strip().split(":")[1].replace(" ", ""))
        record = int(f.readline().strip().split(":")[1].replace(" ", ""))

        print(time)
        print(record)

        winners = 0
        for speed in range(1, time):
            distance = (time - speed) * speed
            if distance > record:
                winners += 1

        print(winners)


star2()
