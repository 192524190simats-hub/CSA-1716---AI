from collections import deque

# Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Possible movements of blank space
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def solve_puzzle(start):
    queue = deque()
    queue.append((start, []))

    visited = set()
    visited.add(start)

    while queue:
        state, path = queue.popleft()

        # Check goal
        if state == goal:
            return path + [state]

        zero = state.index(0)
        row = zero // 3
        col = zero % 3

        for dr, dc in moves:
            new_row = row + dr
            new_col = col + dc

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_zero = new_row * 3 + new_col

                new_state = list(state)

                # Swap blank with the new position
                new_state[zero], new_state[new_zero] = \
                    new_state[new_zero], new_state[zero]

                new_state = tuple(new_state)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [state]))

    return None


# Initial state
start = (1, 2, 3,
         4, 0, 5,
         7, 8, 6)
solution = solve_puzzle(start)

if solution:
    print("Solution found!")
    print("Number of moves:", len(solution) - 1)

    for state in solution:
        print()
        print(state[0], state[1], state[2])
        print(state[3], state[4], state[5])
        print(state[6], state[7], state[8])
else:
    print("No solution found.")
