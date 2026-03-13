NORTH = 1
EAST  = 2
SOUTH = 4
WEST  = 8

from src.maze import Maze
from src.display import draw


def test():
    maze = Maze(20, 15)
    maze.entree = (0,0)
    maze.sortie = (19,14)
    maze.place_42_pattern()
    maze.generate(3)
    draw(maze)


if __name__ == "__main__":
    test()
    # print("██████")
    # print("█    █")
    # print("█    █")
    # print("██████")

