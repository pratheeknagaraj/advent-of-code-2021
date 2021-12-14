#!/usr/bin/python3

import copy

from collections import defaultdict

with open('14_input', 'r') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

polymer = lines[0]

rules = lines[2:]
rule_dict = {}

for r in rules:
    front, back = r.split('->')
    rule_dict[front.strip()] = back.strip()

element_counter = defaultdict(int)
pair_counter = defaultdict(int)

for e in polymer:
    element_counter[e] += 1

for i in range(len(polymer) - 1):
    pair_counter[polymer[i:i+2]] += 1

def step(element_counter, pair_counter):
    new_pair_counter = copy.copy(pair_counter)
    for pair, multiplicity in pair_counter.items():
        insert_element = rule_dict[pair]
        left_pair = pair[0] + insert_element
        right_pair = insert_element + pair[1]
        element_counter[insert_element] += multiplicity
        new_pair_counter[pair] -= multiplicity
        new_pair_counter[left_pair] += multiplicity
        new_pair_counter[right_pair] += multiplicity

    return element_counter, new_pair_counter

steps = 40
for s in range(steps):
    element_counter, pair_counter = step(element_counter, pair_counter)

    counts = element_counter.values()

print(max(counts) - min(counts))
