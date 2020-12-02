#!/usr/bin/env python3
import sys

def passes(line):
    first, second, password = line.split()
    lower, upper = map(int, first.split('-'))
    letter = second[:-1]
    return lower <= password.count(letter) <= upper

print(sum(passes(line) for line in sys.stdin if line))
