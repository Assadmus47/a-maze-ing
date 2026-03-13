
from src.maze import Maze
from src.display import draw
import random

def menu(maze, seed) -> None:
    choice: int = 0
    while(choice != 4):
        try:
            draw(maze)
            print()
            print()
            print("=== A-Maze-ing ===")
            print("1. Re-generate a new maze")
            print("2. Show/hide path from entry to exit")
            print("4. Rotate maze colors")
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
            print("chemin est afficher")
        elif choice == 3:
            print("color changed")
        elif choice == 4:
            print("close")
            return

def main():
    maze = Maze(20, 15)
    maze.entree = (0,0)
    maze.sortie = (19,14)
    maze.place_42_pattern()
    maze.generate(8)
    menu(maze, 42)


if __name__ == "__main__":
    main()