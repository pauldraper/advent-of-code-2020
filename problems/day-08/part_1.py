#!/usr/bin/env python3
import sys

instructions = []
for line in sys.stdin:
    type_, ins = line.split()
    instructions.append([type_, int(ins)])

s = set()
i = 0
acc = 0
while True:
    s.add(i)
    if instructions[i][0] == "nop":
        i += 1
    elif instructions[i][0] == "acc":
        acc += instructions[i][1]
        i += 1
    elif instructions[i][0] == "jmp":
        i += instructions[i][1]
    if i in s:
        print(acc)
        break
