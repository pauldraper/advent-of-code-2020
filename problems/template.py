#!/usr/bin/env python3
import sys

data = []
for line in sys.stdin:
    if not line:
        continue
    line = line.rstrip("\n")
    data.append(line)

print()
