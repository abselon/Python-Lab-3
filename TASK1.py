# TASK 1
# Implementation of Breadth-First Search and Depth-First Search algorithms for a graph or tree data structure.

my_graph = {
    5: [3, 7],
    3: [2, 4],
    7: [8],
    2: [],
    4: [8],
    8: []
}

my_tree = {
    100: [50, 150],    #Root node 100
    50: [25, 75],
    25: [10, 30],
    10: [5, 15],
    5: [],
    15: [],
    30: [],
    75: [60, 80],
    60: [],
    80: [90],
    90: [],
    150: [125, 175],
    125: [110, 130],
    110: [],
    130: [135],
    135: [],
    175: [165, 180],
    165: [],
    180: [190],
    190: []
}

visited_nodes = []  # List to keep track of visited nodes.
queue = []  # Initialize a queue


def breadth_first_traversal(visited, graph_or_tree, start_node):  # function for BFS
    visited.append(start_node)
    queue.append(start_node)

    while len(queue) > 0:          # Creating loop to visit each node
        current_node = queue.pop(0)
        print(current_node, end=" ")

        for neighbour in graph_or_tree[current_node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Driver Code
print("Breadth-First Search Traversal of the tree:")
breadth_first_traversal(visited_nodes, my_tree, 100)    # function calling


visited_nodes = set()  # Set to keep track of visited nodes of graph.


def depth_first_traversal(visited, graph_or_tree, start_node):  # function for dfs
    if start_node not in visited:
        print(start_node)
        visited.add(start_node)
        for neighbour in graph_or_tree[start_node]:
            depth_first_traversal(visited, graph_or_tree, neighbour)


# Driver Code
print("\nDepth-First Search Traversal of the tree:")
depth_first_traversal(visited_nodes, my_tree, 100)
