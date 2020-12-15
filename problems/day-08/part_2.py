#!/usr/bin/env python3
import sys

instructions = []
for line in sys.stdin:
    type_, ins = line.split()
    instructions.append([type_, int(ins)])


def flip(instruction):
    if instruction[0] == "nop":
        instruction[0] = "jmp"
    elif instruction[0] == "jmp":
        instruction[0] = "nop"


for j in range(len(instructions)):
    flip(instructions[j])
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
        if i == len(instructions):
            print(acc)
            break
        if i > len(instructions) or i in s:
            break
    flip(instructions[j])
