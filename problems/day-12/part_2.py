#!/usr/bin/env python3
import sys

x, y = 0, 0
x2, y2 = 10, 1

for line in sys.stdin:
    action = line[0]
    amount = int(line[1:])
    if action == "N":
        y2 += amount
    elif action == "S":
        y2 -= amount
    elif action == "E":
        x2 += amount
    elif action == "W":
        x2 -= amount
    elif action == "L":
        for _ in range(0, amount, 90):
            x2, y2 = -y2, x2
    elif action == "R":
        for _ in range(0, amount, 90):
            x2, y2 = y2, -x2
    elif action == "F":
        x += x2 * amount
        y += y2 * amount

print(abs(x) + abs(y))
