#!/usr/bin/env python3
import sys

rules = {}
for line in sys.stdin:
    if line == "\n":
        break
    num_text, subrules_text = line.split(": ")
    subrules = [s.split(" ") for s in subrules_text.split(" | ")]
    rules[int(num_text)] = subrules


def match_rule(i, line):
    for subrule in rules[i]:
        if not subrule[0].startswith('"'):
            yield from match_subrule(subrule, 0, line)
        elif line and subrule[0][1] == line[0]:
            yield line[1:]


def match_subrule(subrule, j, line):
    if j >= len(subrule):
        yield line
        return
    for match in match_rule(int(subrule[j]), line):
        yield from match_subrule(subrule, j + 1, match)


count = sum("" in match_rule(0, line.rstrip("\n")) for line in sys.stdin)
print(count)
