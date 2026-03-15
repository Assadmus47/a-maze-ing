
NORTH = 1
EAST  = 2
SOUTH = 4
WEST  = 8

CYAN = "\033[36m"
RESET = "\033[0m"
YELLOW = "\033[33m"
RED = "\033[31m"
GREEN   = "\033[32m"
MAGENTA = "\033[95m"


def display_wall(maze, wall, x, y, end):
    if (x, y) in maze.forty_two:
        print(CYAN + wall + RESET, end=end)
    else:
        print(YELLOW + wall + RESET, end=end)


def draw(maze) -> None:
    
    for y in range (maze.height):
        for x in range(maze.width):
            if maze.has_wall(x, y, NORTH):
                display_wall(maze, "▓▓▓▓▓", x ,y, "")
            else:
                print(YELLOW + "▓    " + RESET, end="")

        display_wall(maze, "▓", x, y, "\n")
        

        for _ in range(2):
            for x in range(maze.width):
                if maze.has_wall(x, y, WEST):
                    if (x, y) in maze.forty_two:
                        print(CYAN + "▓▓▓▓▓" + RESET, end="")
                    elif (x, y) == maze.entree:
                        print(YELLOW + "▓" + MAGENTA + "████" + RESET, end="")
                    elif hasattr(maze, "path") and (x, y) in maze.path:
                        print(YELLOW + " " + GREEN + "████" + RESET, end="")
                    elif (x, y) == maze.sortie:
                        print(YELLOW + "▓" + RED + "████" + RESET, end="")
                    else:
                        print(YELLOW + "▓    " + RESET, end="")
                else:
                    if (x, y) == maze.entree:
                        print(" " + MAGENTA + "████" + RESET, end="")
                    elif (x, y) == maze.sortie:
                        print(YELLOW + " " + RED + "████" + RESET, end="")
                    else:
                        print(YELLOW + "     " + RESET, end="")
            display_wall(maze, "▓", x, y, "\n")

    for x in range(maze.width):
        display_wall(maze, "▓▓▓▓▓", x, y, "")

    display_wall(maze, "▓", x, y, "\n")
