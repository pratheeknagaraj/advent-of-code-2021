#!/usr/bin/python3

with open('02_input', 'r') as f:
    lines = f.readlines()

dirs = [n.strip().split() for n in lines]

horizontal = 0
depth = 0

for d, n_str in dirs:
    n = int(n_str)
    if d == 'forward':
        horizontal += n
    elif d == 'down':
        depth += n
    elif d == 'up':
        depth -= n

val = horizontal * depth
print(val)
