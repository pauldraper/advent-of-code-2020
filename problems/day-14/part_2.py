#!/usr/bin/env python3
import sys


def resolve(b, i=0):
    if len(b) <= i:
        yield ""
        return
    for a in resolve(b, i + 1):
        if b[i] == "F":
            yield "0" + a
            yield "1" + a
        else:
            yield b[i] + a


memory = {}


for line in sys.stdin:
    parts = line.split()

    if parts[0] == "mask":
        mask = parts[2]
        continue

    address_bin = format(int(parts[0][4:-1]), "b").zfill(len(mask))
    address_bin = "".join(
        b if mask[i] == "0" else "1" if mask[i] == "1" else "F"
        for i in enumerate(address_bin)
    )
    value = int(parts[2])

    for a in resolve(address_bin):
        memory[int(a, 2)] = value

print(sum(memory.values()))
