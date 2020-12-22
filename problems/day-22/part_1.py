#!/usr/bin/env python3
import sys
import itertools

next(sys.stdin)
p1 = [int(line) for line in itertools.takewhile(lambda line: line != "\n", sys.stdin)]

next(sys.stdin)
p2 = [int(line) for line in sys.stdin]


while p1 and p2:
    c1 = p1.pop(0)
    c2 = p2.pop(0)
    if c2 < c1:
        p1 += [c1, c2]
    else:
        p2 += [c2, c1]

s = sum((i + 1) * c for i, c in enumerate(reversed(p1 + p2)))

print(s)
