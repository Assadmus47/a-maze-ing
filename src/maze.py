
import random

NORTH = 1
EAST  = 2
SOUTH = 4
WEST  = 8

OPPOSITE = {
    NORTH: SOUTH,
    EAST: WEST,
    WEST: EAST,
    SOUTH: NORTH
}

DIRECTIONS = {
    NORTH: (0, -1),
    SOUTH: (0, 1),
    EAST: (1, 0),
    WEST: (-1, 0),
}

class Maze:
    """Represents the maze grid.

    Attributes:
        width: The width of the maze in cells.
        height: The height of the maze in cells.
        grid: 2D list containing wall data for each cell.
    """
    def __init__(self, width: int, height: int) -> None:
        """Initializes the maze grid with all walls closed.

        Args:
            width: The number of cells horizontally.
            height: The number of cells vertically.
        """
        self.width: int = width
        self.height: int = height
        self.grid: list[list[int]] = [[0xF for _ in range(width)] for _ in range(height)]

    def has_wall(self, x: int, y: int, direction: int) -> bool:
        """check if there is a wall in the direction given as a parameter.

        Args:
            x: column.
            y: row.
            direction: the direction that we want if there is a wall on it or no.

        Returns:
            returns bool result True if there is a wall , False if there isnt.
        """
        return bool(self.grid[y][x] & direction)

    def remove_wall(self, x: int, y: int, direction: int) -> None:
        """Remove a wall in the direction given as a parameter.

        Args:
            x: column.
            y: row.
            direction: the direction that we want if there is a wall on it or no.
        """
        self.grid[y][x] &= ~direction
        dx, dy = DIRECTIONS[direction]
        direction = OPPOSITE[direction]
        self.grid[y + dy][x + dx] &= ~direction

    def generate(self, seed: int) -> None:
        random.seed(seed)

        stack = []
        visited = set()

        visited.add((0, 0))
        stack.append((0, 0))