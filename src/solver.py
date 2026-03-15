from collections import deque
from src.maze import DIRECTIONS


def solve(maze):

    start = maze.entree
    goal = maze.sortie

    queue = deque([start])
    visited = {start}
    came_from = {}

    while queue:

        x, y = queue.popleft()

        if (x, y) == goal:
            break

        for direction, (dx, dy) in DIRECTIONS.items():

            if maze.has_wall(x, y, direction):
                continue

            nx = x + dx
            ny = y + dy

            if (nx, ny) in visited:
                continue

            visited.add((nx, ny))
            came_from[(nx, ny)] = (x, y)
            queue.append((nx, ny))

    path = [goal]
    current = goal

    if goal not in came_from:
        return []

    while current != start:
        current = came_from[current]
        path.append(current)

    path.reverse()

    return path