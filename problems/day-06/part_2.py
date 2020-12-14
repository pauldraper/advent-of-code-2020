#!/usr/bin/env python3
import sys

count = 0
for group in sys.stdin.read().split("\n\n"):
    first, *rest = [set(line) for line in group.split()]
    count += len(first.intersection(*rest))
print(count)
