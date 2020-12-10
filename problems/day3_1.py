#!/usr/bin/env python3
import sys

grid = [["#" == c for c in line.strip()] for line in sys.stdin if line]

count = 0
for i in range(1, len(grid)):
    row = grid[i]
    if row[i * 3 % len(row)]:
        count += 1
print(count)
