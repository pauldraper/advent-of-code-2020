#!/usr/bin/env python3
import itertools
import sys

start = int(next(sys.stdin))
buses = [int(text) for text in next(sys.stdin).strip().split(",") if text != "x"]

for time in itertools.count(start=start):
    for bus in buses:
        if not time % int(bus):
            print((time - start) * bus)
            break
    else:
        continue
    break
