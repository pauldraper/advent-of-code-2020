#!/usr/bin/env python3
import sys

seats = []
for line in sys.stdin:
    line = line.replace("F", "0").replace("B", "1")
    line = line.replace("L", "0").replace("R", "1")
    seats.append(int(line, 2))

print(max(seats))
