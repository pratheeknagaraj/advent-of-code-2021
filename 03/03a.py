#!/usr/bin/python3

with open('03_input', 'r') as f:
    lines = f.readlines()

bits_list = [list(n.strip()) for n in lines]

bit_len = len(bits_list[0])

zeros = [0 for i in range(bit_len)]
ones = [0 for i in range(bit_len)]

for bits in bits_list:
    for i, b in enumerate(bits):
        if b == '0':
            zeros[i] += 1
        elif b == '1':
            ones[i] += 1

most = ''
least = ''

for i in range(bit_len):
    if zeros[i] > ones[i]:
        most += '0'
        least += '1'
    else:
        most += '1'
        least += '0'


int_most = int(most, 2)
int_least = int(least, 2)

val = int_most * int_least

print(val)
