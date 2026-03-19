
def write_output(filename: str, maze) -> None:

    with open(filename, "w", encoding="utf-8") as f:

        for row in maze.grid:
            line = "".join(format(cell, "X") for cell in row)
            f.write(line + "\n")

        f.write("\n")

        f.write(f"{maze.entree[0]},{maze.entree[1]}\n")
        f.write(f"{maze.sortie[0]},{maze.sortie[1]}\n")

        path = path_to_directions(maze.path_list)
        f.write(path + "\n")


def path_to_directions(path):

    directions = []

    for i in range(len(path) - 1):

        x1, y1 = path[i]
        x2, y2 = path[i + 1]

        dx = x2 - x1
        dy = y2 - y1

        if dx == 1:
            directions.append("E")
        elif dx == -1:
            directions.append("W")
        elif dy == 1:
            directions.append("S")
        elif dy == -1:
            directions.append("N")

    return "".join(directions)
