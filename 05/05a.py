#!/usr/bin/python3

with open('05_input', 'r') as f:
    lines = f.readlines()

point_map = {}

dir_list = []
for l in lines:
    parts = l.strip().split()
    start = tuple([int(i) for i in parts[0].split(',')])
    end = tuple([int(i) for i in parts[2].split(',')])
    dir_list.append((start, end))

for d in dir_list:
    # Horizontal and Vertical Only
    start, end = d
    points = None
    if start[0] == end[0]:
        if start[1] > end[1]:
            points = [(start[0], y) for y in range(end[1], start[1] + 1)]
        else:
            points = [(start[0], y) for y in range(start[1], end[1] + 1)]
    elif start[1] == end[1]:
        if start[0] > end[0]:
            points = [(x, start[1]) for x in range(end[0], start[0] + 1)]
        else:
            points = [(x, start[1]) for x in range(start[0], end[0] + 1)]
    
    if points:
        for p in points:
            point_map[p] = point_map.get(p, 0) + 1

count = 0

for p, n in point_map.items():
    if n >= 2:
        count += 1

print(count)
