from collections import deque

def solve():
    start = (3, 3, 1)
    goal = (0, 0, 0)

    queue = deque([(start, [])])
    visited = set()

    moves = [(1, 0), (2, 0), (0, 1),
             (0, 2), (1, 1)]

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)
        m, c, boat = state

        path = path + [state]

        if state == goal:
            for step in path:
                print(step)
            return

        for dm, dc in moves:
            if boat == 1:
                new_state = (m - dm, c - dc, 0)
            else:
                new_state = (m + dm, c + dc, 1)

            nm, nc, nb = new_state

            if not (0 <= nm <= 3 and 0 <= nc <= 3):
                continue

            left_m, left_c = nm, nc
            right_m, right_c = 3 - nm, 3 - nc

            if (left_m == 0 or left_m >= left_c) and \
               (right_m == 0 or right_m >= right_c):

                if new_state not in visited:
                    queue.append((new_state, path))

    print("No solution found")

solve()
