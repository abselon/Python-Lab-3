import time
import random

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def insert_node(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert_node(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert_node(root.left, node)

def bfs(root, val):
    queue = []
    queue.append(root)
    while len(queue) > 0:
        current_node = queue.pop(0)
        if current_node.val == val:
            return True
        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)
    return False

def dfs(root, val):
    if root is None:
        return False
    if root.val == val:
        return True
    return dfs(root.left, val) or dfs(root.right, val)

# Set 1: Generate random and unique numbers between 1000 and 40000
set1 = set()
while len(set1) < 100:
    set1.add(random.randint(1000, 40000))

# Set 2: Generate random and unique numbers between 40000 and 80000
set2 = set()
while len(set2) < 100:
    set2.add(random.randint(40000, 80000))

# Set 3: Generate random and unique numbers between 80000 and 200000
set3 = set()
while len(set3) < 100:
    set3.add(random.randint(80000, 200000))

# Set 4: Generate random and unique numbers between 200000 and 1000000
set4 = set()
while len(set4) < 100:
    set4.add(random.randint(200000, 1000000))

# Set 5: Generate random and unique numbers between 1000 and 1000000
set5 = set()
while len(set5) < 100:
    set5.add(random.randint(1000, 1000000))

# Build the trees for each set
root1 = None
root2 = None
root3 = None
root4 = None
root5 = None

for val in set1:
    node = Node(val)
    if root1 is None:
        root1 = node
    else:
        insert_node(root1, node)

for val in set2:
    node = Node(val)
    if root2 is None:
        root2 = node
    else:
        insert_node(root2, node)

for val in set3:
    node = Node(val)
    if root3 is None:
        root3 = node
    else:
        insert_node(root3, node)

for val in set4:
    node = Node(val)
    if root4 is None:
        root4 = node
    else:
        insert_node(root4, node)

for val in set5:
    node = Node(val)
    if root5 is None:
        root5 = node
    else:
        insert_node(root5, node)

# BFS and DFS search for each set and calculate time taken
start_time = time.time()
for val in set1:
    bfs(root1, val)
end_time = time.time()
print(f"Set 1 BFS execution time: {end_time - start_time} seconds")

start_time = time.time()
for val in set1:
    bfs(root2, val)
end_time = time.time()
print(f"Set 2 BFS execution time: {end_time - start_time} seconds")

start_time = time.time()
for val in set1:
    bfs(root3, val)
end_time = time.time()
print(f"Set 1 BFS execution time: {end_time - start_time} seconds")

start_time = time.time()
for val in set1:
    bfs(root4, val)
end_time = time.time()
print(f"Set 1 BFS execution time: {end_time - start_time} seconds")

start_time = time.time()
for val in set1:
    bfs(root5, val)
end_time = time.time()
print(f"Set 1 BFS execution time: {end_time - start_time} seconds")
