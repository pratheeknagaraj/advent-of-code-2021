#!/usr/bin/python3

with open('10_input', 'r') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

def score(line):
    lifo_queue = []

    for i in range(len(line)):
        char = line[i]

        if char in ('(','<','[','{'):
            lifo_queue.append(char)
        elif char in (')','>',']','}'):
            peek = lifo_queue[-1]
            if char == ')' and peek != '(':
                return 3
            if char == ']' and peek != '[':
                return 57
            if char == '}' and peek != '{':
                return 1197
            if char == '>' and peek != '<':
                return 25137
            
            lifo_queue.pop(-1)

    return 0

total = 0

for l in lines:
    s = score(l)
    total += s

print(total)
