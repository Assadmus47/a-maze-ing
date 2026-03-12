NORTH = 1
EAST  = 2
SOUTH = 4
WEST  = 8

from src.maze import Maze


def test():
    maze = Maze(20, 15)
    maze.generate(99, True)
    for i in range (15):
        for j in range(20):
            print(maze.grid[i][j], end="")
        print()
    maze1 = Maze(20, 15)
    print()
    maze1.generate(99, False)
    for i in range (15):
        for j in range(20):
            print(maze1.grid[i][j], end="")
        print()

    


if __name__ == "__main__":
    test()
