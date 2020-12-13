#!/usr/bin/env python3
import sys

next(sys.stdin)
buses = next(sys.stdin).strip().split(",")

start = 0
period = 1
for diff, text in enumerate(buses):
    if text == "x":
        continue
    this_period = int(text)
    while (start + diff) % this_period:
        start += period
    period *= this_period

print(start)
