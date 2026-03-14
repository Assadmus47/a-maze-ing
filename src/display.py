
from .maze import Maze

NORTH = 1
EAST = 2
SOUTH = 4
WEST = 8
RESET = "\033[0m"


def display_wall(
        maze: Maze, wall: str, x: int, y: int, end: str, color: list[str]
) -> None:
    """Prints walls with two differant colors depending
    on the cell if it is in the forty_two set of the maze object

    Args:
        maze: maze object
        wall: string of wall contain this char ▓ or space
        x: column
        y: row
        end: end of print none or \n
        color: list of colors
    """
    if (x, y) in maze.forty_two:
        print(color[0] + wall + RESET, end=end)
    else:
        print(color[1] + wall + RESET, end=end)


def draw(maze: Maze, color: list[str]) -> None:
    """Draw the maze using this char: ▓ and space
    to draw walls and
    use ansii codes to colorize some walls.

    Args:
        maze: maze object
        color: list of colors
    """
    for y in range(maze.height):
        for x in range(maze.width):
            if maze.has_wall(x, y, NORTH):
                display_wall(maze, "▓▓▓▓▓", x, y, "", color)
            else:
                print(color[1] + "▓    " + RESET, end="")

        display_wall(maze, "▓", x, y, "\n", color)

        for _ in range(2):
            for x in range(maze.width):
                if maze.has_wall(x, y, WEST):
                    if (x, y) in maze.forty_two:
                        print(color[0] + "▓▓▓▓▓" + RESET, end="")

                    elif (x, y) == maze.entree:
                        print(
                            color[1] + "▓" + color[3] + "████" + RESET,
                            end=""
                            )

                    elif (x, y) == maze.sortie:
                        print(
                            color[1] + "▓" + color[2] + "████" + RESET,
                            end=""
                            )

                    else:
                        print(color[1] + "▓    " + RESET, end="")
                else:
                    if (x, y) == maze.entree:
                        print(" " + color[3] + "████" + RESET, end="")
                    elif (x, y) == maze.sortie:
                        print(
                            color[1] + " " + color[2] + "████" + RESET,
                            end=""
                            )
                    else:
                        print(color[1] + "     " + RESET, end="")
            display_wall(maze, "▓", x, y, "\n", color)

    for x in range(maze.width):
        display_wall(maze, "▓▓▓▓▓", x, y, "", color)

    display_wall(maze, "▓", x, y, "\n", color)
