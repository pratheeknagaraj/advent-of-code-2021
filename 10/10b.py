#!/usr/bin/python3

with open('10_input', 'r') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

def is_corrupted(line):
    lifo_queue = []

    for i in range(len(line)):
        char = line[i]

        if char in ('(','<','[','{'):
            lifo_queue.append(char)
        elif char in (')','>',']','}'):
            peek = lifo_queue[-1]
            if char == ')' and peek != '(':
                return True
            if char == ']' and peek != '[':
                return True
            if char == '}' and peek != '{':
                return True
            if char == '>' and peek != '<':
                return True
            
            lifo_queue.pop(-1)

    return False

def score_incomplete(line):
    lifo_queue = []

    for i in range(len(line)):
        char = line[i]

        if char in ('(','<','[','{'):
            lifo_queue.append(char)
        elif char in (')','>',']','}'):
            lifo_queue.pop(-1)

    rev_chars = lifo_queue[::-1]

    vals = {'(': 1, '[': 2, '{': 3, '<': 4}

    score = 0
    for i in range(len(rev_chars)):
        char = rev_chars[i]
        score *= 5
        score += vals[char]

    return score

scores = []

for l in lines:
    corrupted = is_corrupted(l)
    if not corrupted:
        s = score_incomplete(l)
        scores.append(s)

count_incomplete = len(scores)
scores = sorted(scores)
median_score = scores[count_incomplete // 2]
print(median_score)

