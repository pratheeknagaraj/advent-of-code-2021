#!/usr/bin/python3

with open('11_input', 'r') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

class State:

    def __init__(self, lines):
        self.step = 0
        self.make_grid(lines)
        self.flash_count = 0

    def make_grid(self, lines):
        self.grid = []
        for l in lines:
            self.grid.append([int(i) for i in  list(l)])
        self.width = len(self.grid[0])
        self.height = len(self.grid)

    def make_step(self):
       
        to_flash = []

        for y in range(self.height):
            for x in range(self.width):
                self.grid[y][x] += 1
                if self.grid[y][x] >= 10:
                    to_flash.append((x,y))

        flashed = set()

        while to_flash:
            cell = to_flash.pop(0)
            flashed.add(cell)
            self.flash_count += 1
            x, y = cell
            self.grid[y][x] = 0

            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    if i == 0 and j == 0:
                        continue
                    new_x, new_y = i + x, j + y
                    new_cell = (new_x, new_y)
                    if 0 <= new_x < self.width and 0 <= new_y < self.height:
                        if new_cell not in flashed:
                            self.grid[new_y][new_x] += 1
                            if self.grid[new_y][new_x] >= 10 and new_cell not in to_flash:
                                to_flash.append(new_cell)

        self.step += 1    

    def print_state(self):
        print(f"State: {self.step}")
        for j in range(self.height):
            print(''.join([str(i) for i in self.grid[j]]))
        print(self.flash_count)
        print()

state = State(lines)

for i in range(100):
    state.make_step()

print(state.flash_count)

