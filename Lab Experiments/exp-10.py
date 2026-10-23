graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Estimated cost to the goal F
h = {
    'A': 6,
    'B': 5,
    'C': 3,
    'D': 4,
    'E': 1,
    'F': 0
}

def astar(start, goal):
    open_list = [(h[start], 0, start, [start])]
    best_cost = {start: 0}

    while open_list:
        open_list.sort()
        f, g, node, path = open_list.pop(0)

        if node == goal:
            print("Path:", path)
            print("Cost:", g)
            return

        if g > best_cost[node]:
            continue

        for neighbour, cost in graph[node]:
            new_g = g + cost

            if neighbour not in best_cost or new_g < best_cost[neighbour]:
                best_cost[neighbour] = new_g
                new_f = new_g + h[neighbour]

                open_list.append(
                    (new_f, new_g, neighbour, path + [neighbour])
                )

    print("No path found")

astar('A', 'F')
