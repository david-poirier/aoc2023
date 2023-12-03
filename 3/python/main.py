import re


def main():
    rows = []
    with open("../input.txt") as f:
        for line in f:
            line = line.strip()
            rows.append(line)

    total = 0
    for y in range(len(rows)):
        row = rows[y]
        for match in re.finditer(r"\d+", row):
            span_0, span_1 = match.span()
            span_0 = max(0, span_0 - 1)
            span_1 = min(len(row), span_1 + 1)
            not_found = True
            # look above
            if y > 0:
                above = rows[y - 1][span_0:span_1]
                if above != "." * len(above):
                    print("above", match, y, above)
                    total += int(match.group())
                    not_found = False
            # look below
            if not_found and y < len(rows) - 1:
                below = rows[y + 1][span_0:span_1]
                if below != "." * len(below):
                    print("below", match, y, below)
                    total += int(match.group())
                    not_found = False
            # before
            if not_found and match.start() > 0:
                if row[match.start() - 1] != ".":
                    print("before", match, y, row[match.start() - 1])
                    total += int(match.group())
                    not_found = False
            # after
            if not_found and match.end() < len(row):
                if row[match.end()] != ".":
                    print("after", match, y, row[match.end()])
                    total += int(match.group())
                    not_found = False
    print(total)


def star2():
    numbers = {}
    symbols = {}

    with open("../input.txt") as f:
        y = 0
        for line in f:
            line = line.strip()
            for match in re.finditer(r"\d+", line):
                for x in range(match.start(), match.end()):
                    numbers[(y, x)] = match
            for match in re.finditer(r"[^\d.]", line):
                symbols[y, match.start()] = match
            y += 1

    total = 0
    for location, match in symbols.items():
        y, x = location
        if match.group() == "*":
            parts = []
            # above
            for offset in range(-1, 2):
                search = (y - 1, x + offset)
                if search in numbers and numbers[search] not in parts:
                    parts.append(numbers[search])
            # below
            for offset in range(-1, 2):
                search = (y + 1, x + offset)
                if search in numbers and numbers[search] not in parts:
                    parts.append(numbers[search])
            # before
            search = (y, x - 1)
            if search in numbers and numbers[search] not in parts:
                parts.append(numbers[search])
            # after
            search = (y, x + 1)
            if search in numbers and numbers[search] not in parts:
                parts.append(numbers[search])

            if len(parts) == 2:
                total += int(parts[0].group()) * int(parts[1].group())

    print(total)

star2()
