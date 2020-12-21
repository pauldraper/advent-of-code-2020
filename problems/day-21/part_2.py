#!/usr/bin/env python3
import collections
import operator
import sys

Food = collections.namedtuple("Food", ["ingredients", "allergens"])

foods = []
for line in sys.stdin:
    igr_text, alg_text = line.rstrip("\n")[:-1].split(" (contains ")
    igrs = igr_text.split(" ")
    algs = alg_text.split(", ")
    foods.append(Food(set(igrs), set(algs)))

allergens = list({alg for food in foods for alg in food.allergens})

possible = {}
for alg in allergens:
    possible[alg] = set.intersection(
        *(food.ingredients for food in foods if alg in food.allergens)
    )


solution = {}


def solve(i):
    if len(allergens) <= i:
        return True
    for igr in possible[allergens[i]] - set(solution.values()):
        solution[allergens[i]] = igr
        if solve(i + 1):
            return True
        del solution[allergens[i]]


solve(0)

print(",".join(solution[alg] for alg in sorted(solution)))
