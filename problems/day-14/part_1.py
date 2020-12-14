#!/usr/bin/env python3
import sys

memory = {}


for line in sys.stdin:
    parts = line.split()

    if parts[0] == "mask":
        mask = parts[2]
        continue

    address = int(parts[0][4:-1])
    value_bin = format(int(parts[2]), "b").zfill(len(mask))
    value_bin = "".join(
        b if mask[i] == "X" else mask[i] for i, b in enumerate(value_bin)
    )

    memory[address] = int(value_bin, 2)

print(sum(memory.values()))
