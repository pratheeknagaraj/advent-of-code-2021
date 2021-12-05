#!/usr/bin/python3

with open('04_input', 'r') as f:
    lines = f.readlines()

num_list = [int(n) for n in lines[0].strip().split(',')]

lines = lines[2:]

class Board:

    def __init__(self, lines):
        self.called = [[False for i in range(5)] for j in range(5)]
        
        self.remaining = set()
        self.pos_map = dict()

        for i, l in enumerate(lines):
            for j, x in enumerate(l.split()):
                n = int(x)
                self.remaining.add(n)
                self.pos_map[n] = (i,j)

    def call(self, n):
        if n in self.pos_map:
            i, j = self.pos_map[n]
            self.called[i][j] = True
            self.remaining.remove(n)

        if self.check_win():
            return self.get_score(n)
        else:
            return None

    def check_win(self):
        for i in range(5):
            if all(self.called[i]):
                return True
            if all([c[i] for c in self.called]):
                return True
        return False

    def get_score(self, n):
        return sum(self.remaining) * n

boards = []
new_board = []

for l in lines:
    if l.strip() == '':
        b = Board(new_board)
        boards.append(b)
        new_board = []
    else:
        new_board.append(l.strip())

done = False
for n in num_list:
    for b in boards:
        res = b.call(n)
        if res:
            print(res)
            done = True
            break
    if done:
        break
