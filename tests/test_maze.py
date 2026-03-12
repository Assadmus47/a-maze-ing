NORTH = 1
EAST  = 2
SOUTH = 4
WEST  = 8

from src.maze import Maze


def test():
    maze = Maze(20, 15)
    maze.place_42_pattern()
    maze.generate(99, True)
    for i in range (15):
        for j in range(20):
            if maze.grid[i][j] == 15:
                print("o", end="")
            else:
                print(" ", end="")
        print()


    


if __name__ == "__main__":
    test()

