#!/usr/bin/env python3
import sys

grid = [list(line.rstrip()) for line in sys.stdin]


def occupied(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == "#"


change = True
while change:
    change = False
    new_grid = [list(row) for row in grid]
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == ".":
                continue
            count = sum(
                occupied(i + k, j + l) for k in [-1, 0, 1] for l in [-1, 0, 1] if k or l
            )
            if count == 0:
                new_grid[i][j] = "#"
            elif count >= 4:
                new_grid[i][j] = "L"
            if new_grid[i][j] != cell:
                change = True
    grid = new_grid

print(sum(cell == "#" for row in grid for cell in row))
