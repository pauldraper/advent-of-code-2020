#!/usr/bin/env python3
import sys

expenses = [int(line) for line in sys.stdin if line]
for i, a in enumerate(expenses):
    for j, b in enumerate(expenses[i + 1:], i + 1):
        for k, c in enumerate(expenses[j + 1:], j + 1):
            if a + b + c == 2020:
                print(a * b * c)
