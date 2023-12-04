import re


class Card:
    def __init__(self, line: str):
        line = line.strip()
        header, body = tuple(line.split(": "))
        _, self.id = tuple(header.split())
        self.id = int(self.id)
        winners, yours = tuple(body.split(" | "))
        self.winners = winners.split()
        self.yours = yours.split()

        self.copies = 1

    def score(self):
        matches = self.matches()
        if matches == 0:
            return 0
        elif matches == 1:
            return 1
        else:
            return pow(2, matches - 1)

    def matches(self):
        total = 0
        for y in self.yours:
            if y in self.winners:
                total += 1
        return total


def star1():
    total = 0
    with open("../input.txt") as f:
        for line in f:
            card = Card(line)
            total += card.score()
    print(total)


def star2():
    cards = {}
    with open("../input.txt") as f:
        for line in f:
            card = Card(line)
            cards[card.id] = card

    for card in cards.values():
        print(card.id, card.copies)
        if card.matches() > 0:
            for _ in range(0, card.copies):
                for _id in range(card.id + 1, card.id + card.matches()+1):
                    if _id in cards:
                        cards[_id].copies += 1
        #print(card.id, card.matches(), card.copies)

    copies = 0
    for card in cards.values():
        #print(card.id, card.copies)
        copies += card.copies
    print(copies)


star2()
