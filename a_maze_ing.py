
from src.maze import Maze
from src.display import draw
from src.config_parser import load_config
import random
import sys

def menu(maze, seed) -> None:
    choice: int = 0
    path = None
    while(choice != 4):
        try:
            draw(maze)
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
            print("error:", e)
        
        if choice == 1:
            maze = Maze(20, 15)
            maze.entree = (random.randint(0, 19),random.randint(0, 14))
            maze.sortie = (random.randint(0, 19),random.randint(0, 14))
            maze.place_42_pattern()
            maze.generate(random.randint(0, 99999))
        elif choice == 2:
            maze.solve()
            input("appuie sur entree pour afficher le chemin")
        elif choice == 3:
            print("color changed")
        elif choice == 4:
            print("close")
            return

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py config.txt")
        return

    config_file = sys.argv[1]

    config = load_config(config_file)

    maze = Maze(config["width"], config["height"])

    maze.entree = config["entry"]
    maze.sortie = config["exit"]

    maze.place_42_pattern()
    maze.generate(config["seed"], config["perfect"])

    menu(maze, config["seed"])


if __name__ == "__main__":
    main()