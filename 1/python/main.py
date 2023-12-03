import sys
import timeit

DIGIT_MAP = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_digit(line: str, mode: int, direction: int) -> int:
    if direction > 0:
        # left to right
        pos = 0
        while True:
            if line[pos].isdigit():
                return int(line[pos])
            if mode == 2:
                for digit_name, digit_num in DIGIT_MAP.items():
                    if line[pos : pos + len(digit_name)] == digit_name:
                        return digit_num
            pos += 1
    else:
        # right to left
        pos = len(line) - 1
        while True:
            if line[pos].isdigit():
                return int(line[pos])
            if mode == 2:
                for digit_name, digit_num in DIGIT_MAP.items():
                    if line[pos - len(digit_name) + 1 : pos + 1] == digit_name:
                        return digit_num
            pos -= 1


def main(mode: int, silent=False, verbose=False):
    total = 0
    with open("input.txt") as f:
        for line in f:
            line = line.strip()

            first_digit = get_digit(line, mode, 1)
            last_digit = get_digit(line, mode, -1)
            val = first_digit * 10 + last_digit
            total += val
            if verbose:
                print(line, first_digit, last_digit, val, total)

    if not silent:
        print(f"mode {mode} total:", total)


if __name__ == "__main__":
    for mode in [2]:
        main(mode=mode, verbose=True)
        break
        print(
            f"mode {mode} timeit (100):",
            timeit.timeit(lambda: main(mode=mode, silent=True), number=100),
        )
