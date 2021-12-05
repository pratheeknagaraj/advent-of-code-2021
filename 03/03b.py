#!/usr/bin/python3

import copy

with open('03_input', 'r') as f:
    lines = f.readlines()

bits_list = [list(n.strip()) for n in lines]

bit_len = len(bits_list[0])

oxy = None
co2 = None

oxy_list = copy.deepcopy(bits_list)
co2_list = copy.deepcopy(bits_list)

for i in range(bit_len):
    zeros = sum([1 for a in oxy_list if a[i] == '0'])
    ones = sum([1 for a in oxy_list if a[i] == '1'])

    most = '1' if ones >= zeros else '0'

    oxy_list = [n for n in oxy_list if n[i] == most]
    
    if len(oxy_list) == 1:
        oxy = ''.join(oxy_list[0])
        break

for i in range(bit_len):
    zeros = sum([1 for a in co2_list if a[i] == '0'])
    ones = sum([1 for a in co2_list if a[i] == '1'])

    least = '0' if zeros <= ones else '1'

    co2_list = [n for n in co2_list if n[i] == least]
    
    if len(co2_list) == 1:
        co2 = ''.join(co2_list[0])
        break

int_oxy = int(oxy, 2)
int_co2 = int(co2, 2)

val = int_oxy * int_co2

print(val)
