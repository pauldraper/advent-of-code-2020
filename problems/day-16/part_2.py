#!/usr/bin/env python3
import numpy
import sys

# definitions
names = []
definitions = []
for line in sys.stdin:
    if line == "\n":
        break
    name, condition = line.split(":")
    names.append(name)
    parts = condition.split(" or ")
    ranges = [tuple(map(int, part.split("-"))) for part in parts]
    definitions.append(ranges)

# your
next(sys.stdin)
your = list(map(int, next(sys.stdin).split(",")))
next(sys.stdin)

tickets = [your]

# nearby
next(sys.stdin)
for line in sys.stdin:
    ticket = list(map(int, line.split(",")))
    if all(
        any(a <= n <= b for ranges in definitions for a, b in ranges) for n in ticket
    ):
        tickets.append(ticket)

# solve
fields = []
for i in range(len(your)):
    options = []
    for name, ranges in zip(names, definitions):
        if all(any(a <= t[i] <= b for a, b in ranges) for t in tickets):
            options.append(name)
    fields.append(options)

indices = sorted(range(len(fields)), key=lambda i: len(fields[i]))
fields = sorted(fields, key=lambda f: len(f))

solution = []


def solve(i=0):
    if len(fields) <= i:
        return True
    for option in fields[i]:
        if option not in solution:
            solution.append(option)
            if solve(i + 1):
                return True
            solution.pop()


solve()

print(
    numpy.prod(
        [your[i] for i, name in zip(indices, solution) if name.startswith("departure ")]
    )
)
