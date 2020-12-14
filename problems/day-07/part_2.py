#!/usr/bin/env python3
import functools
import sys

bags = {}
for line in sys.stdin:
    parts = line.split()
    root = tuple(parts[0:2])
    contains = []
    for i in range(4, len(parts), 4):
        if parts[i] == "no":
            break
        count = int(parts[i])
        contains.append((count, tuple(parts[i + 1 : i + 3])))
    bags[root] = contains


@functools.lru_cache(maxsize=None)
def f(color):
    return 1 + sum(f(c) * count for count, c in bags[color])


print(f(("shiny", "gold")) - 1)
