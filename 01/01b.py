#!/usr/bin/python3

with open('01_input', 'r') as f:
    lines = f.readlines()

nums = [int(n.strip()) for n in lines]

prev_window = []
window_size = 3

increase_count = 0

for n in nums:
    if len(prev_window) < window_size:
        prev_window.append(n)
    else:
        new_sum = sum(prev_window[1:]) + n
        if new_sum > sum(prev_window):
            increase_count += 1
        prev_window = prev_window[1:] + [n]

print(increase_count)
