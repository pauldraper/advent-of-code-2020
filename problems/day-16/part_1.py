#!/usr/bin/env python3
import numpy
import sys

# definitions
names = []
definitions = []
for line in sys.stdin:
    if line == "\n":
        break
    _, condition = line.split(":")
    parts = condition.split(" or ")
    ranges = [tuple(map(int, part.split("-"))) for part in parts]
    definitions.append(ranges)

# your
next(sys.stdin)
next(sys.stdin)
next(sys.stdin)

# nearby
s = 0
next(sys.stdin)
for line in sys.stdin:
    ticket = list(map(int, line.split(",")))
    for n in ticket:
        if not any(a <= n <= b for ranges in definitions for a, b in ranges):
            s += n

print(s)
