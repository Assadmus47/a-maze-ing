NORTH = 1
EAST  = 2
SOUTH = 4
WEST  = 8

from src.maze import Maze


def test():
    maze = Maze(5, 3)
    for i in range (3):
        for j in range(5):
            print(maze.grid[i][j], end="")
        print()
    maze.remove_wall(1,1, WEST)
    print(maze.has_wall(1,1, WEST))
    print(maze.has_wall(0,1, EAST))
    


if __name__ == "__main__":
    test()
