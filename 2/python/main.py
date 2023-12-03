class Subset:
    def __init__(self, subset: str):
        self.colours = []
        for colour in subset.split(", "):
            self.colours.append(Colour(colour))


class Colour:
    def __init__(self, colour: str):
        self.count, self.name = tuple(colour.split(" "))
        self.count = int(self.count)


class Game:
    def __init__(self, line: str):
        header, body = tuple(line.split(": "))
        _, self.id = tuple(header.split(" "))
        self.id = int(self.id)
        self.subsets = []
        for subset in body.split("; "):
            self.subsets.append(Subset(subset))

    def power(self):
        red = 0
        green = 0
        blue = 0

        for s in self.subsets:
            for c in s.colours:
                if c.name == "red" and c.count > red:
                    red = c.count
                if c.name == "green" and c.count > green:
                    green = c.count
                if c.name == "blue" and c.count > blue:
                    blue = c.count

        print(red, green, blue)
        return red * green * blue


def is_possible(g: Game):
    for subset in g.subsets:
        for colour in subset.colours:
            if colour.name == "red" and colour.count > 12:
                return False
            if colour.name == "green" and colour.count > 13:
                return False
            if colour.name == "blue" and colour.count > 14:
                return False

    return True


def star1():
    total = 0
    with open("../input.txt") as f:
        for line in f:
            line = line.strip()
            g = Game(line)
            if is_possible(g):
                print(g.id)
                total += g.id

    print(total)

def star2():
    total = 0
    with open("../example.txt") as f:
        for line in f:
            line = line.strip()
            g = Game(line)
            total += g.power()

    print(total)

if __name__ == "__main__":
    star2()
