#!/usr/bin/python3

with open('09_input', 'r') as f:
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

        low_points.append((val, i, j))

def flood_fill(low, i, j):
    dirs = ((-1,0),(1,0),(0,-1),(0,1))
    cells = set()
    queue = [(i,j)]

    while queue:
        cur = queue.pop(0)
        cells.add(cur)
        for d in dirs:
            y, x = cur[0] + d[0], cur[1] + d[1]
            if 0 <= y < rows and 0 <= x < cols:
                val = grid[y][x]
                if val != 9:
                    pos = (y, x)
                    if pos not in cells:
                        queue.append(pos)

    return len(cells)

basin_sizes = []

for l in low_points:
    val, i, j = l
    basin_size = flood_fill(val, i, j)
    basin_sizes.append(basin_size)

sorted_basin_sizes = sorted(basin_sizes, reverse=True)
a, b, c = sorted_basin_sizes[:3]
total = a * b * c
print(total)
