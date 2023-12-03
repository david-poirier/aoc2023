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
            if not_found and y < len(rows)-1:
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


main()
