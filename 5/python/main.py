import sys
from typing import Any, Dict, IO, List


class Range:
    def __init__(self, data: str):
        data = list(map(lambda d: int(d), data.split()))
        self.destination = data[0]
        self.source = data[1]
        self.length = data[2]
        self.source_end = self.source + self.length
        self.offset = self.destination - self.source


class Map:
    def __init__(self, f: IO[Any]):
        self.ranges: List[range] = []
        self.range_min = sys.maxsize
        self.range_max = 0

        while True:
            line = f.readline()
            if line == "" or line.strip() == "":
                break

            r = Range(data=line.strip())
            if self.range_min > r.source:
                self.range_min = r.source
            if self.range_max < r.source_end:
                self.range_max = r.source_end

            self.ranges.append(r)


    def map(self, v: int) -> int:
        if v > self.range_max or v < self.range_min:
            return v
    
        for r in self.ranges:
            if r.source <= v < r.source_end:
                return v + r.offset
        return v


def star2():
    min_loc: int = sys.maxsize

    seeds: List[int]
    maps: Dict[str, Map] = {}

    with open("../input.txt") as f:
        seeds = f.readline()
        seeds = list(map(lambda s: int(s), seeds[7:].split()))
        print(seeds)

        for line in f:
            line = line.strip()
            if line == "":
                continue

            section = line.split()[0]
            maps[section] = Map(f)

    for i in range(0, len(seeds), 2):
        start = seeds[i]
        length = seeds[i+1]
        print(start, length)
        _maps = maps.values()
        for x in range(start, start + length):
            #print("seed", x)
            for v in _maps:
                x = v.map(x)
                #print(k, x)
            if x < min_loc:
                min_loc = x

    print("min location", min_loc)



star2()
