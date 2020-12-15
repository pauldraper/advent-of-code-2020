#!/usr/bin/env python3
import sys

x, y = 0, 0
dx, dy = 1, 0

for line in sys.stdin:
    action = line[0]
    amount = int(line[1:])
    if action == "N":
        y += amount
    elif action == "S":
        y -= amount
    elif action == "E":
        x += amount
    elif action == "W":
        x -= amount
    elif action == "L":
        for _ in range(0, amount, 90):
            dx, dy = -dy, dx
    elif action == "R":
        for _ in range(0, amount, 90):
            dx, dy = dy, -dx
    elif action == "F":
        x += dx * amount
        y += dy * amount

print(abs(x) + abs(y))
