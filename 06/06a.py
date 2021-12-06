#!/usr/bin/python3

with open('06_input', 'r') as f:
    lines = f.readlines()

states = [int(i) for i in lines[0].strip().split(',')]

cache = {}

def fish(timer, days):
    fishes = [timer]
    for i in range(days):
        new = fishes.count(0)
        fishes += [9] * new
        fishes = [f - 1 for f in fishes]
        fishes = [6 if f == -1 else f for f in fishes]
    return len(fishes)

total = 0

day_count = 80
for s in states:
    if s not in cache:
        count = fish(s, day_count)
        cache[s] = count
    total += cache[s]

print(total)
