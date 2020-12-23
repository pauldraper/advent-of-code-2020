#!/usr/bin/env pypy
import sys

cups = list(map(int, sys.stdin.read()))
for x in range(100):
    cups, removed = cups[:1] + cups[4:], cups[1:4]
    label = cups[0]
    while True:
        label -= 1
        if not label:
            label = 9
        if label not in removed:
            break
    i = cups.index(label)
    cups = cups[:(i + 1)] + removed + cups[(i + 1):]
    cups = cups[1:] + cups[:1]

i = cups.index(1)
print(''.join(map(str, cups[(i + 1):] + cups[:i])))
