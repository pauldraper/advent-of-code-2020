#!/usr/bin/env pypy
import sys


class Cup:
    def __init__(self, value):
        self.next = None
        self.value = value

input = sys.stdin.read()
total = 1000 * 1000

lookup = {}
prev = None
for i in range(total):
    value = int(input[i]) if i < len(input) else i + 1
    cup = Cup(value)
    lookup[value] = cup
    if prev:
        prev.next = cup
    else:
        first = cup
    prev = cup
prev.next = first

current = first
for x in range(10 * 1000 * 1000):
    removed = current.next
    current.next = removed.next.next.next
    label = current.value
    while True:
        label -= 1
        if not label:
            label = total
        if label not in (removed.value, removed.next.value, removed.next.next.value):
            break
    dest = lookup[label]
    removed.next.next.next = dest.next
    dest.next = removed
    current = current.next

one = lookup[1]
print(one.next.value * one.next.next.value)
