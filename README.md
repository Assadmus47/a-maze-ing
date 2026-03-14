*This project has been created as part of the 42 curriculum by mkacemi, elbarry.*

# A-Maze-ing

A maze generator and solver written in Python 3.10+, featuring terminal ASCII rendering, a "42" pattern hidden inside the maze, and an interactive menu.

---

## Description

A-Maze-ing generates random mazes from a configuration file and displays them visually in the terminal. Each maze is encoded using a hexadecimal wall representation, can be perfect (single path between entry and exit) or imperfect (multiple paths), and always contains a hidden "42" pattern drawn with fully closed cells at its center.

**Features:**
- Random maze generation with reproducibility via seed
- Perfect and imperfect maze modes
- Hidden "42" pattern embedded in the maze
- Terminal ASCII rendering with ANSI colors
- Interactive menu: regenerate, show/hide path, rotate colors, quit
- Exportable output file in hexadecimal format
- Reusable `mazegen` pip package

---

## Instructions

### Requirements

- Python 3.10 or later
- pip

### Installation

```bash
# Install dependencies (flake8, mypy)
make install
```

### Run

```bash
# Run with a config file
make run
# or directly
python3 a_maze_ing.py config.txt
```

### Debug

```bash
make debug
```

### Lint

```bash
make lint
# or stricter version
make lint-strict
```

### Clean

```bash
make clean
```

---

## Configuration file format

The configuration file uses `KEY=VALUE` pairs, one per line. Lines starting with `#` are comments.

| Key | Description | Example |
|-----|-------------|---------|
| `WIDTH` | Maze width (number of cells) | `WIDTH=20` |
| `HEIGHT` | Maze height (number of cells) | `HEIGHT=15` |
| `ENTRY` | Entry coordinates (x,y) | `ENTRY=0,0` |
| `EXIT` | Exit coordinates (x,y) | `EXIT=19,14` |
| `OUTPUT_FILE` | Output filename | `OUTPUT_FILE=maze.txt` |
| `PERFECT` | Perfect maze (single path)? | `PERFECT=True` |
| `SEED` | Seed for reproducibility (optional) | `SEED=42` |

Example `config.txt`:
```
# A-Maze-ing configuration
WIDTH=20
HEIGHT=15
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=True
SEED=42
```

---

## Maze generation algorithm

**Algorithm chosen: Recursive Backtracker (DFS)**

The maze is generated using the Depth-First Search (DFS) algorithm with an explicit stack (no recursion), also known as the Recursive Backtracker.

**How it works:**
1. Start from cell (0,0), mark it as visited, push it onto the stack
2. While the stack is not empty:
   - Look at the current cell (top of stack)
   - Find all valid unvisited neighbors
   - If neighbors exist: pick one at random, remove the wall between them, mark it visited, push it onto the stack
   - If no neighbors: pop the stack (backtrack)
3. When the stack is empty, every cell has been visited

**Why DFS?**
- Simple to implement and understand
- Guarantees full connectivity — every cell is reachable
- Naturally generates perfect mazes (single path between any two cells)
- Produces mazes with long winding corridors, which are visually interesting
- Easy to justify and explain during peer evaluation

**PERFECT=False mode:**
After DFS, 20% of cells randomly have an additional wall removed, creating loops and multiple paths.

---

## The "42" pattern

Before generation, a "42" pattern is drawn at the center of the grid by forcing certain cells to `0xF` (all walls closed) and adding them to the visited set. The DFS then generates paths around them, leaving the "42" visually intact.

The pattern is 7 cells wide and 5 cells tall. If the maze is too small to contain it, an error message is displayed and the pattern is skipped.

---

## Output file format

Each cell is encoded as one hexadecimal digit, where each bit represents a wall:

| Bit | Direction |
|-----|-----------|
| 0 (LSB) | North |
| 1 | East |
| 2 | South |
| 3 | West |

- `1` = wall closed, `0` = wall open
- Cells stored row by row, one row per line
- After an empty line: entry coordinates, exit coordinates, shortest path (N/E/S/W letters)

---

## Code reusability — mazegen package

The maze generation logic is packaged as a reusable pip package called `mazegen`.

### Install the package

```bash
pip install mazegen-1.0.0-py3-none-any.whl
```

### Basic usage

```python
from src.maze import Maze

# Create a maze
maze = Maze(20, 15)

# Place the "42" pattern
maze.place_42_pattern()

# Generate the maze with a seed
maze.generate(seed=42, perfect=True)

# Access the grid
print(maze.grid)       # 2D list of integers (wall data)
print(maze.width)      # 20
print(maze.height)     # 15
print(maze.visited)    # set of all visited cells

# Check walls
maze.has_wall(x=0, y=0, direction=1)   # True/False (1=NORTH)

# Remove a wall manually
maze.remove_wall(x=0, y=0, direction=2)  # removes EAST wall
```

### Custom parameters

```python
# Custom size
maze = Maze(width=30, height=20)

# Custom seed for reproducibility
maze.generate(seed=99)          # always same maze
maze.generate(seed=99)          # identical result

# Imperfect maze (multiple paths)
maze.generate(seed=42, perfect=False)
```

### Build the package from source

```bash
pip install build
python3 -m build
# Output: dist/mazegen-1.0.0-py3-none-any.whl and dist/mazegen-1.0.0.tar.gz
```

---

## Team and project management

### Roles

| Member | Responsibilities |
|--------|-----------------|
| **mkacemi** | Maze grid structure, DFS generation algorithm, "42" pattern, terminal ASCII display, interactive menu, Makefile, pyproject.toml |
| **elbarry** | config.txt parser, BFS shortest path algorithm, hexadecimal output file |

### Planning

<!-- À compléter avec elbarry -->

### What worked well

- DFS implementation was clean and fast to develop step by step
- Bit encoding for walls made the grid compact and efficient
- ANSI color system with multiple palettes gives a great visual result
- Separating `maze.py` and `display.py` kept the code modular

### What could be improved

<!-- À compléter en fin de projet -->

### Tools used

- **Claude (Anthropic)** — used as a pedagogical guide throughout the project: explaining concepts (DFS, BFS, bit encoding, stack), guiding implementation step by step, reviewing code logic. All code was written and understood by the students.
- **VSCode** with Pylance extension for development
- **flake8** and **mypy** for code quality
- **Git** with feature branches per member

---

## Resources

- [Maze generation algorithms — Wikipedia](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
- [Recursive Backtracker explained — Think Labyrinth](https://www.astrolog.org/labyrnth/algrithm.htm)
- [BFS algorithm — Wikipedia](https://en.wikipedia.org/wiki/Breadth-first_search)
- [Python type hints — mypy documentation](https://mypy.readthedocs.io/)
- [PEP 257 — Docstring conventions](https://peps.python.org/pep-0257/)
- [ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code)

█
