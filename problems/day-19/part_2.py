#!/usr/bin/env python3
import sys

rules = {}
for line in sys.stdin:
    if line == "\n":
        break
    num_text, subrules_text = line.split(": ")
    subrules = [s.split(" ") for s in subrules_text.split(" | ")]
    rules[int(num_text)] = subrules

rules[8] = [["42"], ["42", "8"]]
rules[11] = [["42", "31"], ["42", "11", "31"]]


def match_rule(i, line, depth):
    for subrule in rules[i]:
        if not subrule[0].startswith('"'):
            yield from match_subrule(subrule, 0, line, depth - 1)
        elif line and subrule[0][1] == line[0]:
            yield line[1:]


def match_subrule(subrule, j, line, depth):
    if depth <= 0:
        return
    if j >= len(subrule):
        yield line
        return
    for match in match_rule(int(subrule[j]), line, depth - 1):
        yield from match_subrule(subrule, j + 1, match, depth - 1)


count = sum("" in match_rule(0, line.rstrip("\n"), 100) for line in sys.stdin)
print(count)
