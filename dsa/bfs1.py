from collections import deque

def bfs_shortest_path(graph, start, goal):
    # Maintain a queue of paths
    queue = deque([[start]])
    # Set of visited nodes to prevent revisiting
    visited = set()

    while queue:
        # Get the first path from the queue
        path = queue.popleft()
        # Get the last node from the path
        node = path[-1]

        # Path found
        if node == goal:
            return path

        # Node has not been visited
        elif node not in visited:
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

            # Mark node as visited
            visited.add(node)

    # No path found
    return None

# Example usage
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

start_node = 'A'
goal_node = 'H'
path = bfs_shortest_path(graph, start_node, goal_node)
print(f"Shortest path from {start_node} to {goal_node} is: {path}")
