NORTH = 1
EAST  = 2
SOUTH = 4
WEST  = 8

from src.maze import Maze
from src.display import draw
from src.solver import solve

def test():
    maze = Maze(20, 15)
    maze.entree = (0,0)
    maze.sortie = (19,14)
    maze.place_42_pattern()
    maze.generate(8)
    draw(maze)

    path = solve(maze)
    print("entrée:", maze.entree)
    print("sortie:", maze.sortie)
    print("Chemin trouvé :")
    print(path)
    print(len(path))

if __name__ == "__main__":
    test()
    # print("██████")
    # print("█    █")
    # print("█    █")
    # print("██████")

