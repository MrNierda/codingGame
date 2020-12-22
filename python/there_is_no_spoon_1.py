import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

nodes = []

non_existing_neighbor = "-1 -1"

def get_right_neighbor(node):
    x = node[0] + 1

    while x < width:
        if (x, node[1]) in nodes:
            return f"{x} {node[1]}"
        x += 1

    return non_existing_neighbor

def get_below_neighbor(node):
    y = node[1] + 1

    while y < height:
        if (node[0], y) in nodes:
            return f"{node[0]} {y}"
        y += 1

    return non_existing_neighbor

def get_nodes():
    for i in range(height):
        line = input() 
        
        for j in range(len(line)):
            if line[j] == '0':
                nodes.append((int(j), int(i)))
get_nodes()

for node in nodes:
    print(f"{node[0]} {node[1]} {get_right_neighbor(node)} {get_below_neighbor(node)}")

