#!/usr/bin/env python3
import sys

expenses = set(int(line) for line in sys.stdin if line)
for expense in expenses:
    other = 2020 - expense
    if other in expenses:
        print(expense * other)
        break
