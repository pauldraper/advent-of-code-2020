#!/usr/bin/env pypy
import sys

data = list(map(int, sys.stdin.read().split(",")))
last = {}

previous = None
for i in range(30 * 1000 * 1000):
    if i < len(data):
        answer = data[i]
    elif previous not in last:
        answer = 0
    else:
        answer = i - last[previous]
    last[previous] = i
    previous = answer

print(previous)
