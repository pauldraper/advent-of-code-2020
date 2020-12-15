#!/usr/bin/env python3
import sys

data = list(map(int, sys.stdin))

for i in range(25, len(data)):
    valid = any(data[i] - data[j] in data[:j] for j in range(i - 25, i))
    if not valid:
        print(data[i])
        break
