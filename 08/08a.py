#!/usr/bin/python3

with open('08_input', 'r') as f:
    lines = f.readlines()

displays = []

for l in lines:
    front, back = l.strip().split('|')
    front_digits = front.strip().split()
    back_digits = back.strip().split()
    displays.append((front_digits, back_digits))

count = 0
for display in displays:
    back_digits = display[1]
    for d in back_digits:
        if len(d) in (2, 3, 4, 7):
            count += 1

print(count)
