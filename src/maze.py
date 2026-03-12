
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
    
    def is_valide_neighor(self, x, y, direction, visited):
        dx, dy = DIRECTIONS[direction]
        x += dx
        y += dy

        if (x, y) in visited:
            return False

        
        if self.width - 1 < x or x < 0:
            return False

        if self.height - 1 < y or y < 0:
            return False

        return True

    def generate(self, seed: int, perfect: bool = True) -> None:
        random.seed(seed)

        stack = []
        visited = set()

        visited.add((0, 0))
        stack.append((0, 0))

        while stack:
            x, y = stack[-1]

            valide_neighor = []

            for i in range(4):
                direction = 1 << i
                if self.is_valide_neighor(x, y, direction, visited):
                    valide_neighor.append(direction)

            if not valide_neighor:
                x, y = stack.pop()

            else:
                direction = random.choice(valide_neighor)
                self.remove_wall(x, y, direction)
                dx , dy = DIRECTIONS[direction]
                visited.add((x + dx, y + dy))
                stack.append((x + dx, y + dy))

        if perfect is False:
            for y in range (self.height):
                for x in range(self.width):
                    if random.random() < 0.2:
                        direction = random.choice([NORTH, EAST, SOUTH, WEST])

                        dx, dy = DIRECTIONS[direction]
                        x1 = x + dx
                        y1 = y + dy

                        if self.width - 1 < x1 or x1 < 0:
                            continue

                        if self.height - 1 < y1 or y1 < 0:
                            continue

                        self.remove_wall(x, y, direction)

