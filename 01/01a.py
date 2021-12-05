#!/usr/bin/python3

with open('01_input', 'r') as f:
    lines = f.readlines()

nums = [int(n.strip()) for n in lines]

prev = None

increase_count = 0

for n in nums:
    if prev == None:
        prev = n
    else:
        if n > prev:
            increase_count += 1
        prev = n

print(increase_count)
