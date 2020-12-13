#!/usr/bin/env python3
import sys

grid = [["#" == c for c in line.strip()] for line in sys.stdin]


def count(right, down):
    count = 0
    for i in range(1, (len(grid) - 1) // down + 1):
        row = grid[i * down]
        if row[i * right % len(row)]:
            count += 1
    return count


result = 1
result *= count(1, 1)
result *= count(3, 1)
result *= count(5, 1)
result *= count(7, 1)
result *= count(1, 2)

print(result)
