#!/usr/bin/python3

with open('07_input', 'r') as f:
    lines = f.readlines()

positions = [int(i) for i in lines[0].strip().split(',')]

min_pos = min(positions)
max_pos = max(positions)

def calc_fuel(positions, align):
    return sum([abs(p - align) for p in positions])

min_fuel = sum(positions) * len(positions)
for align_pos in range(min_pos, max_pos + 1):
    fuel = calc_fuel(positions, align_pos)
    if fuel < min_fuel:
        min_fuel = fuel

print(min_fuel)

