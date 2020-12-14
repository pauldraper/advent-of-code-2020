#!/usr/bin/env python3
import collections
import sys

nodes = [0] + sorted(map(int, sys.stdin))
nodes.append(max(nodes) + 3)

counts = collections.Counter(b - a for a, b in zip(nodes, nodes[1:]))

print(counts[1] * counts[3])
