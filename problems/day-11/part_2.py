#!/usr/bin/env python3
import sys

grid = [list(line.rstrip()) for line in sys.stdin]


def occupied(i, j, k, l):
    i2 = i
    j2 = j
    while True:
        i2 += k
        j2 += l
        if not (0 <= i2 < len(grid) and 0 <= j2 < len(grid[i2])):
            return False
        if grid[i2][j2] == "#":
            return True
        elif grid[i2][j2] == "L":
            return False


change = True
while change:
    change = False
    new_grid = [list(row) for row in grid]
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == ".":
                continue
            count = sum(
                occupied(i, j, k, l) for k in [-1, 0, 1] for l in [-1, 0, 1] if k or l
            )
            if count == 0:
                new_grid[i][j] = "#"
            elif count >= 5:
                new_grid[i][j] = "L"
            if new_grid[i][j] != cell:
                change = True
    grid = new_grid

print(sum(cell == "#" for row in grid for cell in row))
