from collections import deque

def bfs_shortest_path(graph, start, goal):
    # Keep track of the explored nodes
    explored = set()
    # Keep track of all the paths to be checked
    queue = deque([[start]])

    # Return path if start is goal
    if start == goal:
        return [start]

    # Loop until there are no more paths to check
    while queue:
        # Get the first path from the queue
        path = queue.popleft()
        # Get the last node from the path
        node = path[-1]

        # If node has not been visited yet
        if node not in explored:
            neighbours = graph[node]
            # Go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # Return path if neighbour is goal
                if neighbour == goal:
                    return new_path

            # Mark node as explored
            explored.add(node)

    # In case there's no path between the 2 nodes
    return None

# Example graph
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': [],
#     'F': []
# }

# graph = {
#     'A': ['B'],
#     'B': ['D', 'E', 'C'],
#     'C': ['D'],
#     'D': ['F'],
#     'E': [],
#     'F': []
# }

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'G'],
    'F': ['C', 'H'],
    'G': ['D', 'E', 'H'],
    'H': ['F', 'G']
}

# Find the shortest path from A to F
# shortest_path = bfs_shortest_path(graph, 'A', 'F')
shortest_path = bfs_shortest_path(graph, 'A', 'H') # Shortest path: ['A', 'C', 'F', 'H']
print("Shortest path:", shortest_path)
