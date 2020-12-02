#!/usr/bin/env python3
import sys

def passes(line):
    first, second, password = line.split()
    start, end = map(int, first.split('-'))
    letter = second[:-1]
    return (password[start - 1] == letter) != (password[end - 1] == letter)

print(sum(passes(line) for line in sys.stdin if line))
