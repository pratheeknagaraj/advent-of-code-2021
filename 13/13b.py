#!/usr/bin/python3

import copy

with open('13_input', 'r') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

points = set()
folds = []
is_folds = False
for l in lines:
    if l == '':
        is_folds = True
        continue
    if not is_folds:
        x, y = l.split(',')
        x, y = int(x), int(y)
        points.add((x,y))
    else:
        axis_str = l.split()[-1]
        axis, intercept = axis_str.split('=')
        folds.append((axis, int(intercept)))

def fold_x(points, val):
    new_points = set()
    for p in points:
        delta = abs(p[0] - val)
        new_x = val - delta
        new_points.add((new_x, p[1]))
    return new_points

def fold_y(points, val):
    new_points = set()
    for p in points:
        delta = abs(p[1] - val)
        new_y = val - delta
        new_points.add((p[0], new_y))
    return new_points

for f in folds:
    direction, val = f[0], f[1]
    if direction == 'x':
        points = fold_x(points, val)
    elif direction == 'y':
        points = fold_y(points, val)

max_x = max([p[0] for p in points])
max_y = max([p[1] for p in points])

for j in range(max_y + 1):
    line = ''
    for i in range(max_x + 1):
        if (i,j) in points:
            line += '#'
        else:
            line += '.'
    print(line)
