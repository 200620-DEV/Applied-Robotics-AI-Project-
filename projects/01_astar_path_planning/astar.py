"""A* path planning on a grid.

The robot in main.py follows a fixed list of moves. Here the robot plans
its own route: A* searches for the shortest path from start to goal while
avoiding obstacles.

Run:  python astar.py
"""
import heapq

GRID_SIZE = 8
OBSTACLES = {(1, 1), (2, 1), (3, 1), (5, 2), (5, 3), (5, 4),
             (1, 5), (2, 5), (3, 5), (3, 4), (6, 6)}
START = (0, 0)
GOAL = (7, 7)

MOVES = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}


def heuristic(a, b):
    """Manhattan distance: never overestimates on a 4-connected grid."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def neighbours(cell):
    x, y = cell
    for dx, dy in MOVES.values():
        nx, ny = x + dx, y + dy
        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and (nx, ny) not in OBSTACLES:
            yield (nx, ny)


def astar(start, goal):
    """Return the list of cells from start to goal, or None if unreachable."""
    open_set = [(heuristic(start, goal), 0, start)]  # (f = g + h, g, cell)
    came_from = {}
    g_cost = {start: 0}

    while open_set:
        _, g, current = heapq.heappop(open_set)
        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]
        if g > g_cost[current]:
            continue  # stale queue entry
        for nxt in neighbours(current):
            new_g = g + 1
            if new_g < g_cost.get(nxt, float("inf")):
                g_cost[nxt] = new_g
                came_from[nxt] = current
                heapq.heappush(open_set, (new_g + heuristic(nxt, goal), new_g, nxt))
    return None


def path_to_commands(path):
    """Turn a list of cells into up/down/left/right commands for the robot."""
    lookup = {v: k for k, v in MOVES.items()}
    return [lookup[(b[0] - a[0], b[1] - a[1])] for a, b in zip(path, path[1:])]


def show(path):
    on_path = set(path or [])
    for y in range(GRID_SIZE):
        row = ""
        for x in range(GRID_SIZE):
            cell = (x, y)
            if cell == START:
                row += "S "
            elif cell == GOAL:
                row += "G "
            elif cell in OBSTACLES:
                row += "# "
            elif cell in on_path:
                row += "* "
            else:
                row += ". "
        print(row)
    print()


if __name__ == "__main__":
    path = astar(START, GOAL)
    if path is None:
        print("No path to the goal.")
    else:
        show(path)
        print("Path length:", len(path) - 1, "moves")
        print("Commands:", path_to_commands(path))
