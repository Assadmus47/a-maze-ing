from .maze import Maze

NORTH = 1
EAST = 2
SOUTH = 4
WEST = 8
RESET = "\033[0m"

DIRECTIONS = {
    NORTH: (0, -1),
    SOUTH: (0, 1),
    EAST: (1, 0),
    WEST: (-1, 0),
}


def display_wall(
        maze: Maze, wall: str, x: int, y: int, end: str, color: list[str]
) -> None:
    """Prints a wall with color depending on if the cell is in forty_two.

    Args:
        maze: maze object
        wall: string of wall chars (▓ or space)
        x: column
        y: row
        end: end of print, none or newline
        color: list of colors
    """
    if (x, y) in maze.forty_two:
        print(color[0] + wall + RESET, end=end)
    else:
        print(color[1] + wall + RESET, end=end)


def draw_cell_west(
        maze: Maze, x: int, y: int, color: list[str], show_path: bool
) -> None:
    """Draw a cell that has a west wall.

    Args:
        maze: maze object
        x: column
        y: row
        color: list of colors
        show_path: whether to display the path
    """
    if (x, y) in maze.forty_two:
        print(color[0] + "▓▓▓▓▓" + RESET, end="")
    elif (x, y) == maze.entree:
        print(color[1] + "▓" + color[3] + "████" + RESET, end="")
    elif (x, y) == maze.sortie:
        print(color[1] + "▓" + color[2] + "████" + RESET, end="")
    elif (x, y) in maze.path and show_path:
        print(color[1] + "▓" + color[4] + "████" + RESET, end="")
    else:
        print(color[1] + "▓    " + RESET, end="")


def draw_cell_no_west(
        maze: Maze, x: int, y: int, color: list[str], show_path: bool
) -> None:
    """Draw a cell that has no west wall.

    Args:
        maze: maze object
        x: column
        y: row
        color: list of colors
        show_path: whether to display the path
    """
    if (x, y) == maze.entree:
        if (x - 1, y) in maze.path and show_path:
            print(color[4] + "█" + color[3] + "████" + RESET, end="")
        else:
            print(" " + color[3] + "████" + RESET, end="")
    elif (x, y) == maze.sortie:
        if (x - 1, y) in maze.path and show_path:
            print(color[4] + "█" + color[2] + "████" + RESET, end="")
        else:
            print(color[1] + " " + color[2] + "████" + RESET, end="")
    elif (x, y) in maze.path and show_path:
        if (x - 1, y) in maze.path:
            print(color[4] + "█████" + RESET, end="")
        else:
            print(color[4] + " ████" + RESET, end="")
    else:
        print(color[1] + "     " + RESET, end="")


def draw(maze: Maze, color: list[str], show_path: bool = False) -> None:
    """Draw the maze using ▓ and space for walls, with ANSI color codes.

    Args:
        maze: maze object
        color: list of colors
        show_path: whether to display the solution path
    """
    for y in range(maze.height):

        # draw north walls row
        for x in range(maze.width):
            if maze.has_wall(x, y, NORTH):
                display_wall(maze, "▓▓▓▓▓", x, y, "", color)
            elif (x, y) in maze.path and show_path:
                if (x, y - 1) in maze.path:
                    print(color[1] + "▓" + color[4] + "████" + RESET, end="")
                else:
                    print(color[1] + "▓" + color[4] + "    " + RESET, end="")
            else:
                print(color[1] + "▓    " + RESET, end="")
        display_wall(maze, "▓", x, y, "\n", color)

        # draw cell body (2 lines tall)
        for _ in range(2):
            for x in range(maze.width):
                if maze.has_wall(x, y, WEST):
                    draw_cell_west(maze, x, y, color, show_path)
                else:
                    draw_cell_no_west(maze, x, y, color, show_path)
            display_wall(maze, "▓", x, y, "\n", color)

    # draw south border
    for x in range(maze.width):
        display_wall(maze, "▓▓▓▓▓", x, y, "", color)
    display_wall(maze, "▓", x, y, "\n", color)
