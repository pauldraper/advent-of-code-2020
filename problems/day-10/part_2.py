#!/usr/bin/env python3
import sys

nodes = [0] + sorted(map(int, sys.stdin))

counts = []
for node in nodes:
    if not counts:
        count = 1
    else:
        count = sum(count for node2, count in zip(nodes, counts) if node <= node2 + 3)
    counts.append(count)

print(counts[-1])
