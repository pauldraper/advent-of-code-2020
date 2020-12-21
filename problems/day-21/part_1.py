#!/usr/bin/env python3
import collections
import sys

Food = collections.namedtuple("Food", ["ingredients", "allergens"])

foods = []
for line in sys.stdin:
    igr_text, alg_text = line.rstrip("\n")[:-1].split(" (contains ")
    igrs = igr_text.split(" ")
    algs = alg_text.split(", ")
    foods.append(Food(set(igrs), set(algs)))

possible = set()
for alg in {alg for food in foods for alg in food.allergens}:
    possible |= set.intersection(
        *(food.ingredients for food in foods if alg in food.allergens)
    )

count = sum(igr not in possible for food in foods for igr in food.ingredients)
print(count)
