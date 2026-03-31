from src import Maze, draw
from src.config_parser import load_config
from src.output_writer import write_output

import sys
import random
from typing import cast

colors = [
    [  # Palette 1
        "\033[36m",  # CYAN
        "\033[33m",  # YELLOW
        "\033[31m",  # RED
        "\033[95m",  # Purple
        "\033[92m"   # GREEN (chemin)
    ],
    [  # Palette 2 -> base vert Pac-Man
        "\033[92m",  # GREEN
        "\033[32m",  # DARK GREEN
        "\033[93m",  # LIGHT YELLOW
        "\033[97m",  # WHITE
        "\033[96m"   # LIGHT CYAN (chemin)
    ],
    [  # Palette 3 -> base bleu foncé Pac-Man
        "\033[34m",  # DARK BLUE
        "\033[94m",  # LIGHT BLUE
        "\033[96m",  # CYAN
        "\033[37m",  # LIGHT GRAY
        "\033[92m"   # GREEN (chemin)
    ],
    [  # Palette 4 -> blanc puis cyan
        "\033[97m",  # WHITE
        "\033[36m",  # CYAN
        "\033[96m",  # LIGHT CYAN
        "\033[90m",  # DARK GRAY
        "\033[92m"   # GREEN (chemin)
    ],
    [  # Palette 5
        "\033[97m",  # WHITE
        "\033[92m",  # GREEN
        "\033[36m",  # CYAN
        "\033[33m",  # YELLOW
        "\033[95m"   # MAGENTA (chemin)
    ],
    [  # Palette 6
        "\033[94m",  # LIGHT BLUE
        "\033[34m",  # DARK BLUE
        "\033[97m",  # WHITE
        "\033[96m",  # LIGHT CYAN
        "\033[92m"   # GREEN (chemin)
    ],
    [  # Palette 7
        "\033[95m",  # MAGENTA
        "\033[35m",  # PURPLE
        "\033[97m",  # WHITE
        "\033[36m",  # CYAN
        "\033[93m"   # LIGHT YELLOW (chemin)
    ],
    [  # Palette 8
        "\033[33m",  # YELLOW
        "\033[91m",  # ORANGE approx
        "\033[36m",  # CYAN
        "\033[97m",  # WHITE
        "\033[92m"   # GREEN (chemin)
    ],
    [  # Palette 9
        "\033[90m",  # DARK GRAY
        "\033[97m",  # WHITE
        "\033[36m",  # CYAN
        "\033[34m",  # DARK BLUE
        "\033[92m"   # GREEN (chemin)
    ],
    [  # Palette 10
        "\033[33m",  # YELLOW
        "\033[90m",  # DARK GRAY
        "\033[36m",  # CYAN
        "\033[97m",  # WHITE
        "\033[92m"   # GREEN (chemin)
    ]
]


def check_entree_exit(maze: Maze, config: dict[str, object]) -> bool:
    entry = cast(tuple[int, int], config["entry"])
    exit_ = cast(tuple[int, int], config["exit"])

    if entry in maze.forty_two:
        print("CHOOSE VALID VALUE OF ENTREE OUTSIDE OF THE 42 PATTERN")
        return False
    if exit_ in maze.forty_two:
        print("CHOOSE VALID VALUE OF EXIT OUTSIDE OF THE 42 PATTERN")
        return False

    return True


def menu(maze: Maze, config: dict[str, object]) -> None:
    choice: int = 0
    color_choice: int = 0
    flage: bool = False

    while choice != 4:
        try:
            draw(maze, colors[color_choice], flage)
            print()
            print()
            print("=== A-Maze-ing ===")
            print("1. Re-generate a new maze")
            print("2. Show/hide path from entry to exit")
            print("3. Rotate maze colors")
            print("4. Quit")
            choice = int(input("Choice? (1-4): "))
            print()

            if choice > 4 or choice < 1:
                print("please enter a choice between 1 and 4")
                continue

        except ValueError as e:
            print()
            print("error:", e)
            continue

        if choice == 1:
            width = cast(int, config["width"])
            height = cast(int, config["height"])
            entry = cast(tuple[int, int], config["entry"])
            exit_ = cast(tuple[int, int], config["exit"])
            perfect = cast(bool, config["perfect"])

            maze = Maze(width, height)
            maze.entree = entry
            maze.sortie = exit_

            maze.place_42_pattern()
            maze.generate(random.randint(0, 99999), perfect)
            maze.solve()

            write_output("maze_output.txt", maze)

        elif choice == 2:
            flage = not flage

        elif choice == 3:
            color_choice = (color_choice + 1) % 10

        elif choice == 4:
            print("close")
            return


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py config.txt")
        return

    config_file = sys.argv[1]

    try:
        config: dict[str, object] = load_config(config_file)
    except Exception as e:
        print("Config error:", e)
        return

    width = cast(int, config["width"])
    height = cast(int, config["height"])

    if width < 9 or height < 7:
        print("Error: maze must be at least 9x7")
        return

    entry = cast(tuple[int, int], config["entry"])
    exit_ = cast(tuple[int, int], config["exit"])
    seed = cast(int, config["seed"])
    perfect = cast(bool, config["perfect"])
    output_file = cast(str, config["output_file"])

    maze = Maze(width, height)
    maze.entree = entry
    maze.sortie = exit_

    maze.place_42_pattern()
    maze.generate(seed, perfect)

    if not check_entree_exit(maze, config):
        return

    maze.solve()
    write_output(output_file, maze)

    menu(maze, config)


if __name__ == "__main__":
    main()
