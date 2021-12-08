#!/usr/bin/python3

with open('08_input', 'r') as f:
    lines = f.readlines()

displays = []

for l in lines:
    front, back = l.strip().split('|')
    front_digits = front.strip().split()
    back_digits = back.strip().split()
    displays.append((front_digits, back_digits))

def solve_display(display):
    front_digits, back_digits = display
    front_sorted = [''.join(sorted(d)) for d in front_digits]
    back_sorted = [''.join(sorted(d)) for d in back_digits]

    one = [d for d in front_sorted if len(d) == 2][0]
    seven = [d for d in front_sorted if len(d) == 3][0]
    four = [d for d in front_sorted if len(d) == 4][0]
    eight = [d for d in front_sorted if len(d) == 7][0]

    nums_2_3_5 = [d for d in front_sorted if len(d) == 5]
    nums_0_6_9 = [d for d in front_sorted if len(d) == 6]

    for i in nums_2_3_5:
        if set(one) < set(i):
            three = i
            break

    for i in nums_0_6_9:
        if set(four) < set(i):
            nine = i
        elif set(seven) < set(i):
            zero = i

    six = [d for d in nums_0_6_9 if d not in (zero, nine)][0]

    for i in nums_2_3_5:
        if set(i) < set(six):
            five = i

    two = [d for d in nums_2_3_5 if d not in (three, five)][0]

    mapping = {
        zero: '0', one: '1', two: '2', three: '3', four: '4',
        five: '5', six: '6', seven: '7', eight: '8', nine: '9'
    }

    num_str = ''
    for d in back_sorted:
        num_str += mapping[d]
    num = int(num_str)

    return num

total = 0
for display in displays:
    num = solve_display(display)
    total += num

print(total)
