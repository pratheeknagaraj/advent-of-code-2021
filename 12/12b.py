#!/usr/bin/python3

import copy

with open('12_input', 'r') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

nodes = dict()

class Node:

    def __init__(self, name):
        self.name = name
        self.edges = set()
        self.is_big = self.name.isupper()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

for line in lines:
    front, back = line.split('-')
    if front not in nodes:
        nodes[front] = Node(front)
    if back not in nodes:
        nodes[back] = Node(back)
    nodes[front].edges.add(nodes[back])
    nodes[back].edges.add(nodes[front])

# Do BFS to discover paths

queue = []
queue.append([nodes['start']])

found_paths = []

def check_doubled(path):
    small_caves = set()
    for node in path:
        if not node.is_big:
            if node in small_caves:
                return True
            small_caves.add(node)
    return False

while queue:
    cur_path = queue.pop(0)
    next_stops = cur_path[-1].edges
    has_doubled = check_doubled(cur_path)

    for next_stop in next_stops:
        if next_stop.name == 'end':
            complete_path = copy.copy(cur_path)
            complete_path += [next_stop]
            found_paths.append(complete_path)
        elif next_stop.is_big:
            new_path = copy.copy(cur_path)
            new_path += [next_stop]
            queue.append(new_path)
        else:
            if (next_stop in cur_path) and (not has_doubled) and (next_stop.name != 'start'):
                new_path = copy.copy(cur_path)
                new_path += [next_stop]
                queue.append(new_path)
            elif next_stop not in cur_path:
                new_path = copy.copy(cur_path)
                new_path += [next_stop]
                queue.append(new_path)

print(len(found_paths))
