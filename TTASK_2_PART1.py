#TASK2 (1)

import random

# Define the input ranges
ranges = [
    (1000, 5000),
    (40000, 60000),
    (80000, 120000),
    (200000, 300000),
    (1000000, 2000000)
]

# Generate random and unique numbers for each range
input_lists = []
for r in ranges:
    n = random.randint(r[0], r[1])
    input_list = []
    while len(input_list) < n:
        x = random.randint(r[0], r[1])
        if x not in input_list:
            input_list.append(x)
    input_lists.append(input_list)

# Build a tree for each input list
for i, input_list in enumerate(input_lists):
    print(f"Input List {i}: {input_list}")
    tree = {}
    for x in input_list:
        node = tree
        for digit in str(x):
            node = node.setdefault(int(digit), {})
    print(f"Tree {i}: {tree}")
