#!/usr/bin/python3

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

def step(polymer):
    insertions = []
    for i in range(len(polymer) - 1):
        pair = polymer[i:i+2]
        insertion = rule_dict.get(pair, '')
        insertions.append(insertion)
    
    new_polymer = ''
    for i in range(len(polymer) - 1):
        new_polymer += polymer[i]
        new_polymer += insertions[i]
    new_polymer += polymer[-1]

    return new_polymer

steps = 10
for s in range(steps):
    polymer = step(polymer)

element_counts = defaultdict(int)
for p in polymer:
    element_counts[p] += 1

counts = element_counts.values()
print(max(counts) - min(counts))

