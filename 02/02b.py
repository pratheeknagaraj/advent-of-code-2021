#!/usr/bin/python3

with open('02_input', 'r') as f:
    lines = f.readlines()

dirs = [n.strip().split() for n in lines]

horizontal = 0
depth = 0
aim = 0

for d, n_str in dirs:
    n = int(n_str)
    if d == 'forward':
        horizontal += n
        depth += n*aim
    elif d == 'down':
        aim += n
    elif d == 'up':
        aim -= n

val = horizontal * depth
print(val)
