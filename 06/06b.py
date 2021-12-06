#!/usr/bin/python3

import math

with open('06_input', 'r') as f:
    lines = f.readlines()

states = [int(i) for i in lines[0].strip().split(',')]

def multiplicity(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n-r)

def fish(timer, days):
    init = timer + 1
    bound = days - init
    count = 1

    max_nums = bound // 7

    if days >= init:
        count += 1

    for n in range(1, max_nums + 1):
        for nines in range(0, n + 1):
            s = 7 * (n - nines) + 9 * nines
            if s <= bound:
                m = multiplicity(n, nines)
                count += m
            else:
                break

    return count
    
cache = {}
total = 0
day_count = 256

for s in states:
    if s not in cache:
        count = fish(s, day_count)
        cache[s] = count
    total += cache[s]

print(total)
