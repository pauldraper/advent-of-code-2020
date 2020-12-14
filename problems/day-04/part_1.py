#!/usr/bin/env python3
import sys
import re

count = 0
for text in sys.stdin.read().split("\n\n"):
    passport = {}
    keys = {part.split(":")[0] for part in text.split()}
    count += {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"} <= keys
print(count)
