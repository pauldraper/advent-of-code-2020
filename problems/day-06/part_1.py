#!/usr/bin/env python3
import sys

count = 0
for group in sys.stdin.read().split("\n\n"):
    count += len(set(group.replace("\n", "")))
print(count)
