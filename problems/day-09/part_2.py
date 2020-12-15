#!/usr/bin/env python3
import sys

data = list(map(int, sys.stdin))

for i in range(25, len(data)):
    valid = any(data[i] - data[j] in data[:j] for j in range(i - 25, i))
    if not valid:
        target = data[i]

for i in range(len(data)):
    for j in range(i + 1, len(data)):
        d = data[i : j + 1]
        if sum(d) == target:
            print(min(d) + max(d))
