import heapq
def astar(graph, start, goal):
    open_list = [(0, start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, goal)

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor, cost in graph[current]:
            tentative_g_score = g_score[current] + cost

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None  # No path found

def heuristic(node, goal):
    # Replace this with your specific heuristic function, e.g., Manhattan distance, Euclidean distance, etc.
    return 0

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.insert(0, current)
    return path

# Example graph representation
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('D', 4), ('E', 2)],
    'C': [('A', 3), ('F', 7)],
    'D': [('B', 4), ('G', 5)],
    'E': [('B', 2), ('H', 3)],
    'F': [('C', 7), ('I', 2)],
    'G': [('D', 5), ('H', 2)],
    'H': [('E', 3), ('G', 2), ('I', 4)],
    'I': [('F', 2), ('H', 4)]
}

start_node = 'A'
goal_node = 'I'

optimum_path = astar(graph, start_node, goal_node)

if optimum_path:
    print("Optimum Path:", optimum_path)
    print("Total Cost:", sum(graph[node][0][1] for node in optimum_path[:-1]))
else:
    print("No path found.")
