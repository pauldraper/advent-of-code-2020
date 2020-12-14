#!/usr/bin/env python3
import sys

bags = {}
for line in sys.stdin:
    parts = line.split()
    root = tuple(parts[0:2])
    contains = []
    for i in range(4, len(parts), 4):
        if parts[i] == "no":
            break
        contains.append(tuple(parts[i + 1 : i + 3]))
    bags[root] = contains


def f(color):
    if color == ("shiny", "gold"):
        return True
    return any(f(c) for c in bags[color])


print(sum(f(color) for color in bags) - 1)
