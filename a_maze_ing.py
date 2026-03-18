
from src import Maze, draw

import random

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

RESET = "\033[0m"


def menu(maze: Maze) -> None:
    choice: int = 0
    color_choice: int = 0
    flage: bool = False
    while (choice != 4):
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
            maze = Maze(20, 15)
            maze.entree = (random.randint(0, 19), random.randint(0, 14))
            maze.sortie = (random.randint(0, 19), random.randint(0, 14))
            maze.place_42_pattern()
            maze.generate(random.randint(0, 99999))
            maze.solve()
        elif choice == 2:
            if flage == True:
                flage = False
            else:
                flage = True
        elif choice == 3:
            color_choice += 1
            if color_choice == 10:
                color_choice = 0
        elif choice == 4:
            print("close")
            return


def main() -> None:
    maze = Maze(20, 15)
    maze.entree = (0, 0)
    maze.sortie = (19, 14)
    maze.place_42_pattern()
    maze.generate(42)
    maze.solve()
    menu(maze)


if __name__ == "__main__":
    main()
