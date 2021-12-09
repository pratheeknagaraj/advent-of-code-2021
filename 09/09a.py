#!/usr/bin/python3

with open('09_input', 'r') as f:
#with open('09_example', 'r') as f:
    lines = f.readlines()

grid = []
for l in lines:
    grid.append([int(i) for i in l.strip()])

rows = len(grid)
cols = len(grid[0])

low_points = []

for i in range(rows):
    for j in range(cols):
        val = grid[i][j]

        if i > 0 and grid[i-1][j] <= val:
            continue
        if i < (rows-1) and grid[i+1][j] <= val:
            continue
        if j > 0 and grid[i][j-1] <= val:
            continue
        if j < (cols-1) and grid[i][j+1] <= val:
            continue

        low_points.append(val)

risk_levels = [l + 1 for l in low_points]
total = sum(risk_levels)
print(total)
