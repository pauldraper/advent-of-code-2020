#!/usr/bin/env python3
import sys
import functools
import itertools

next(sys.stdin)
p1 = tuple(
    int(line) for line in itertools.takewhile(lambda line: line != "\n", sys.stdin)
)

next(sys.stdin)
p2 = tuple(int(line) for line in sys.stdin)


@functools.lru_cache(maxsize=None)
def play(p1, p2):
    cache = set()
    try:
        while p1 and p2:
            d = (p1, p2)
            if d in cache:
                return "1"
            cache.add(d)
            c1, p1 = p1[0], p1[1:]
            c2, p2 = p2[0], p2[1:]
            if c1 <= len(p1) and c2 <= len(p2):
                winner = play(p1[:c1], p2[:c2])
            else:
                winner = "1" if c2 < c1 else "0"
            if winner == "1":
                p1 += (c1, c2)
            else:
                p2 += (c2, c1)
        return "1" if p1 else "0"
    finally:
        global s
        s = sum((i + 1) * c for i, c in enumerate(reversed(p1 + p2)))


play(p1, p2)

print(s)
