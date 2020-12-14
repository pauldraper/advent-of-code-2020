#!/usr/bin/env python3
import sys
import re

count = 0
for text in sys.stdin.read().split("\n\n"):
    passport = {}
    for part in text.split():
        key, value = part.split(":")
        passport[key] = value
    try:
        if not 1920 <= int(passport["byr"]) <= 2002:
            continue
    except:
        continue
    try:
        if not 2010 <= int(passport["iyr"]) <= 2020:
            continue
    except:
        continue
    try:
        if not 2020 <= int(passport["eyr"]) <= 2030:
            continue
    except:
        continue
    try:
        if passport["hgt"].endswith("cm"):
            hgt = int(passport["hgt"][: -len("cm")])
            if not 150 <= hgt <= 193:
                continue
        elif passport["hgt"].endswith("in"):
            inc = int(passport["hgt"][: -len("in")])
            if not 59 <= inc <= 76:
                continue
        else:
            continue
    except:
        continue
    if "hcl" not in passport or not re.fullmatch("#[0-9a-f]{6}", passport["hcl"]):
        continue
    if "ecl" not in passport or passport["ecl"] not in (
        "amb",
        "blu",
        "brn",
        "gry",
        "grn",
        "hzl",
        "oth",
    ):
        continue
    if "pid" not in passport or not re.fullmatch("[0-9]{9}", passport["pid"]):
        continue
    count += 1

print(count)
