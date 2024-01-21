from collections import deque
def water_jug_problem(capacity_x, capacity_y, target):
    visited_states = set()
    initial_state = (0, 0)
    queue = deque([(initial_state, [])])

    while queue:
        state, actions = queue.popleft()
        x, y = state

        if x == target or y == target:
            print("Found a solution:", actions)
            return

        visited_states.add(state)

        # Fill jug X
        if x < capacity_x:
            new_state = (capacity_x, y)
            if new_state not in visited_states:
                queue.append((new_state, actions + ["Fill X"]))

        # Fill jug Y
        if y < capacity_y:
            new_state = (x, capacity_y)
            if new_state not in visited_states:
                queue.append((new_state, actions + ["Fill Y"]))

        # Empty jug X
        if x > 0:
            new_state = (0, y)
            if new_state not in visited_states:
                queue.append((new_state, actions + ["Empty X"]))

        # Empty jug Y
        if y > 0:
            new_state = (x, 0)
            if new_state not in visited_states:
                queue.append((new_state, actions + ["Empty Y"]))

        # Pour from X to Y
        if x > 0 and y < capacity_y:
            amount = min(x, capacity_y - y)
            new_state = (x - amount, y + amount)
            if new_state not in visited_states:
                queue.append((new_state, actions + ["Pour X to Y"]))

        # Pour from Y to X
        if y > 0 and x < capacity_x:
            amount = min(y, capacity_x - x)
            new_state = (x + amount, y - amount)
            if new_state not in visited_states:
                queue.append((new_state, actions + ["Pour Y to X"]))

    print("No solution found.")

# Example usage
capacity_x = 14
capacity_y = 13
target = 9

water_jug_problem(capacity_x, capacity_y, target)
