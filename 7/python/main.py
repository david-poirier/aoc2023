CARDS = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "T",
    "J",
    "Q",
    "K",
    "A",
]


class Hand:
    def __init__(self, data: str):
        self.data = data
        self.cards = []
        self.bid = 0

        cards, bid = data.split()

        for c in cards:
            self.cards.append(CARDS.index(c))

        self.groups = {}
        for c in self.cards:
            if c in self.groups:
                self.groups[c] += 1
            else:
                self.groups[c] = 1

        self.type = 0
        for g in self.groups.values():
            if g == 5:
                self.type = 6
            elif g == 4:
                self.type = 5
            elif g == 3:
                if self.type == 1:
                    self.type = 4
                else:
                    self.type = 3
            elif g == 2:
                if self.type == 3:
                    # already have three of a kind
                    self.type = 4
                elif self.type == 1:
                    # already have pair
                    self.type = 2
                else:
                    self.type = 1

        self.bid = int(bid)

        self.hexvalue = str(self.type)
        for c in self.cards:
            self.hexvalue += format(c, "x")

        self.value = int(self.hexvalue, 16)


def star1():
    hands = []
    with open("../input.txt") as f:
        for line in f:
            line = line.strip()
            hand = Hand(line)
            hands.append(hand)

    hands.sort(key=lambda x: x.value)

    winnings = 0
    rank = 1
    for hand in hands:
        print(hand.data, hand.value, hand.hexvalue)
        winnings += rank * hand.bid
        rank += 1

    print(winnings)


CARDS2 = [
    "J",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "T",
    "X",
    "Q",
    "K",
    "A",
]


class Hand2:
    def __init__(self, data: str):
        self.data = data
        self.cards = []
        self.bid = 0

        cards, bid = data.split()

        wildcards = 0
        for c in cards:
            if c == "J":
                wildcards += 1
            self.cards.append(CARDS2.index(c))

        self.groups = {}
        for c in self.cards:
            if c in self.groups:
                self.groups[c] += 1
            else:
                self.groups[c] = 1

        self.type = 0
        for c, g in sorted(self.groups.items(), key=lambda item: (item[1], item[0]), reverse=True):
            if CARDS2.index("J") == c:
                if g == 5:
                    self.type = 6
                else:
                    continue
            else:
                g += wildcards

            if g == 5:
                self.type = 6
                wildcards = 0
            elif g == 4:
                self.type = 5
                wildcards = 0
            elif g == 3:
                if self.type == 1:
                    self.type = 4
                    wildcards = 0
                else:
                    self.type = 3
                    wildcards = 0
            elif g == 2:
                if self.type == 3:
                    # already have three of a kind
                    self.type = 4
                    wildcards = 0
                elif self.type == 1:
                    # already have pair
                    wildcards = 0
                    self.type = 2
                else:
                    wildcards = 0
                    self.type = 1

        self.bid = int(bid)

        self.hexvalue = str(self.type)
        for c in self.cards:
            self.hexvalue += format(c, "x")

        self.value = int(self.hexvalue, 16)


def star2():
    hands = []
    with open("../input.txt") as f:
        for line in f:
            line = line.strip()
            hand = Hand2(line)
            hands.append(hand)

    hands.sort(key=lambda x: x.value)

    winnings = 0
    rank = 1
    for hand in hands:
        print(hand.data, hand.value, hand.hexvalue)
        winnings += rank * hand.bid
        rank += 1

    print(winnings)


star2()
