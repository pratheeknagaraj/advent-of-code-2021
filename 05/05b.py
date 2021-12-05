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
    start, end = d
    if start[0] > end[0]:
        xs = range(start[0], end[0] - 1, -1)
    elif end[0] > start[0]:
        xs = range(start[0], end[0] + 1)
    else:
        xs = [start[0]] * (abs(end[1] - start[1]) + 1)

    if start[1] > end[1]:
        ys = range(start[1], end[1] - 1, -1)
    elif start[1] < end[1]:
        ys = range(start[1], end[1] + 1)
    else:
        ys = [start[1]] * (abs(end[0] - start[0]) + 1)

    points = [(x, y) for x, y in zip(xs, ys)]

    for p in points:
        point_map[p] = point_map.get(p, 0) + 1

count = 0

for p, n in point_map.items():
    if n >= 2:
        count += 1

print(count)
