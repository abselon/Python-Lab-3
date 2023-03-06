#PART1

from typing import List, Dict, Tuple

def uniform_cost_search(goal_states: List[int], start_state: int, graph: Dict[int, List[int]], cost: Dict[Tuple[int, int], int]) -> List[int]:
    # Initialize the answer list to hold the minimum cost upto the goal state from starting state
    answer = [float('inf') for _ in range(len(goal_states))]

    # Create a priority queue to hold the nodes
    queue = []

    # Insert the starting index
    queue.append((0, start_state))

    # Map to store visited node
    visited = set()

    # Count the number of goals that have been reached
    num_goals_reached = 0

    # While the queue is not empty
    while queue:
        # Get the node with the least cost
        p = min(queue)

        # Pop the element
        queue.remove(p)

        # Check if the element is part of the goal list
        if p[1] in goal_states:
            # Get the index of the goal state
            index = goal_states.index(p[1])

            # If a new goal is reached
            if answer[index] == float('inf'):
                num_goals_reached += 1

            # If the cost is less
            if answer[index] > p[0]:
                answer[index] = p[0]

            # If all goal states have been reached, return the answer
            if num_goals_reached == len(goal_states):
                return answer

        # Check for the non visited nodes
        # which are adjacent to present node
        if p[1] not in visited:
            for node in graph[p[1]]:
                # Add the neighboring nodes to the queue
                queue.append((p[0] + cost[(p[1], node)], node))

        # Mark as visited
        visited.add(p[1])

    return answer


# Test the algorithm
if __name__ == '__main__':
    # Define the graph
    graph = {
        0: [1, 3],
        1: [6],
        2: [1],
        3: [1, 4, 6],
        4: [2, 5],
        5: [2, 6],
        6: [4]
    }

    # Define the cost
    cost = {
        (0, 1): 2,
        (0, 3): 5,
        (1, 6): 1,
        (2, 1): 4,
        (3, 1): 5,
        (3, 4): 2,
        (3, 6): 6,
        (4, 2): 4,
        (4, 5): 3,
        (5, 2): 6,
        (5, 6): 3,
        (6, 4): 7
    }

    # Define the goal state
    goal_states = [6]

    # Define the start state
    start_state = 0

    # Run the algorithm and print the result
    answer = uniform_cost_search(goal_states, start_state, graph, cost)
    print(f"Minimum cost from {start_state} to {goal_states[0]} is = {answer[0]}")


#part2
graph = {} # initialize an empty dictionary to represent the graph/tree
print("Enter the nodes of the graph/tree in the format 'node1 node2' where node2 is a node connected to node1.")
print("Enter 0 0 to terminate input.")
while True:
inp = list(map(int, input().split())) # take input as a list of integers
node1, node2 = inp[0], inp[1]
if node1 == 0 and node2 == 0: # check for termination condition
break
if node1 not in graph.keys(): # add node1 to the dictionary if it does not exist
graph.update({node1: [node2]})
else: # if node1 exists, add node2 to its list
graph[node1].append(node2)
print("The graph is represented as:")
print(graph) # print the final dictionary representation of the graph/tree