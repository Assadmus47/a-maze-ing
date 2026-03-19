*This project has been created as part of the 42 curriculum by elbarry, mkacemi*

# 🌀 A-Maze-ing

---

## 📋 Description

**A-Maze-ing** generates, solves, displays and exports mazes from a configuration file.

The program is built around a reusable maze module and follows this workflow:

1. Read and validate a configuration file
2. Create the maze grid
3. Generate the maze using **Depth-First Search (DFS)** with backtracking
4. Solve the maze using **Breadth-First Search (BFS)**
5. Display the maze in the terminal
6. Export the result to an output file

---

## ⚙️ Requirements

- Python **3.10** or later
- `pip`
- A **UTF-8 compatible terminal** for proper maze rendering

---

## 🚀 Installation

Clone the repository and move into the project directory:

```bash
git clone <repository_url>
cd A-Maze-ing
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Upgrade pip and install the project:

```bash
python3 -m pip install --upgrade pip
python3 -m pip install .
```

---

## ▶️ Running the Project

You can run the project in three ways:

```bash
# Using the main Python file
python3 a_maze_ing.py config.txt

# Or using the installed entry point
mazegen config.txt

# Or using the Makefile rule
make run
```

---

## 📦 Building the Package

```bash
python3 -m pip install build
python3 -m build
```

The generated `.tar.gz` and `.whl` files will appear in the `dist/` directory.

---

## 🧹 Linting & Type Checking

```bash
flake8 .
mypy .

# Or if a Makefile is provided:
make lint
make lint-strict
```

---

## 🗂️ Configuration File

The project reads a configuration file to define maze settings.

### Example

```ini
WIDTH=20
HEIGHT=20
ENTRY=0,0
EXIT=5,9
PERFECT=True
OUTPUT_FILE=maze_output.txt
SEED=46
```

### Parameters

| Key | Type | Required | Description |
|---|---|---|---|
| `WIDTH` | integer | ✅ | Number of columns (strictly positive) |
| `HEIGHT` | integer | ✅ | Number of rows (strictly positive) |
| `ENTRY` | `x,y` | ✅ | Entry point coordinates (must be inside the grid) |
| `EXIT` | `x,y` | ✅ | Exit point coordinates (must differ from ENTRY) |
| `PERFECT` | boolean | ✅ | If `True`, exactly one path exists between any two cells |
| `OUTPUT_FILE` | string | ✅ | Path to the output file where the maze and solution are exported |
| `SEED` | integer | ✅ | Initializes the RNG for deterministic generation |

### Parsing & Validation

The parser:
- Reads the file line by line and splits on `=`
- Converts values to their expected types
- Validates all constraints

Invalid configurations (e.g. `WIDTH=abc`, `ENTRY=100,100`, missing keys) are rejected with a clear error message.

---

## 🏗️ Maze Generation — DFS with Backtracking

The algorithm starts from cell `(0, 0)` and explores the maze by always moving to a valid unvisited neighbor, chosen at random. When no such neighbor exists, it backtracks by popping the stack. This is classic **iterative DFS with backtracking**.

```python
random.seed(seed)
stack = []
self.visited.add((0, 0))
stack.append((0, 0))

while stack:
    x, y = stack[-1]
    valid_neighbors = []

    for i in range(4):
        direction = 1 << i
        if self.is_valid_neighbor(x, y, direction):
            valid_neighbors.append(direction)

    if not valid_neighbors:
        stack.pop()  # backtrack: no unvisited neighbor, go back
    else:
        direction = random.choice(valid_neighbors)
        self.remove_wall(x, y, direction)
        dx, dy = DIRECTIONS[direction]
        self.visited.add((x + dx, y + dy))
        stack.append((x + dx, y + dy))
```

When `PERFECT=False`, an additional pass randomly removes ~20% of extra walls, creating multiple paths between some cells (imperfect maze).

**Why DFS?** Simple, efficient on grids, produces interesting mazes, and naturally demonstrates stacks, backtracking, and random neighbor selection.

---

## 🔍 Maze Solving — BFS (Shortest Path)

BFS explores the maze level by level, guaranteeing the **shortest path** from entry to exit.

```python
queue = deque([start])
visited = {start}
came_from = {}

while queue:
    x, y = queue.popleft()

    if (x, y) == goal:
        break

    for direction, (dx, dy) in DIRECTIONS.items():
        if self.has_wall(x, y, direction):
            continue
        nx, ny = x + dx, y + dy
        if (nx, ny) in visited:
            continue
        visited.add((nx, ny))
        came_from[(nx, ny)] = (x, y)
        queue.append((nx, ny))

# Path reconstruction
path = [goal]
current = goal
while current != start:
    current = came_from[current]
    path.append(current)
path.reverse()

self.path_list = path
self.path = set(path)
```

The path is stored in two forms:
- `path_list` — ordered list for export
- `path` — set for fast terminal display

---

## 🧱 Internal Representation

Each cell is an integer encoding its walls using **bit flags**:

| Direction | Constant | Bit |
|---|---|---|
| NORTH | `1` | `0001` |
| EAST | `2` | `0010` |
| SOUTH | `4` | `0100` |
| WEST | `8` | `1000` |

A cell with walls on NORTH and WEST = `1 + 8 = 9`.

This compact representation allows fast wall checking, addition, and removal.

---

## 📤 Output File

The exported file contains:

- The maze grid in **hexadecimal** format
- Entry and exit coordinates
- The solution path as movement letters (`N`, `S`, `E`, `W`)

### Example

```
D391793953
BAE852C47A
AAFAFAFFFA

0,0
9,7
ESSSSSEESSEEEEEE
```

Path conversion: coordinate differences map to directions (`dx=1 → E`, `dy=1 → S`, etc.)

---

## 🖥️ Terminal Display

```
┌───┬───┬───┬───┐
│ E     │       │
├───┘   └───┬───┤
│       │       │
├───┬───┘   └───┤
│               S│
└───┴───┴───┴───┘
```

`E` = entry · `S` = exit · solution path highlighted

---

## 🔄 Project Workflow

```
config.txt
    ↓
 parsing
    ↓
validation
    ↓
maze generation (DFS)
    ↓
maze solving (BFS)
    ↓
output file export
    ↓
terminal display
```

Every regeneration triggers: **generate → solve → write_output**, keeping the output file always in sync.

---

## 🧩 Reusable Module

The maze engine is fully decoupled from configuration parsing, terminal rendering, and file output. It can be imported independently into:

- A graphical maze visualizer
- A pathfinding test suite
- Another terminal application

---

## 👥 Team and Project Management

### Roles of each team member

**elbarry**
- Project organization and structure
- Testing and code review
- Documentation contributions
- Implementation support

**mkacemi**
- Maze engine implementation (grid, walls, bit representation)
- Configuration parsing and validation logic
- DFS generation and BFS solving integration
- Packaging and terminal rendering behavior

### Tools used

- Python 3, `venv`, `pip`
- `pyproject.toml`, `build`
- `flake8`, `mypy`
- Git
- Terminal-based manual testing
- AI assistance for explanations, packaging guidance, and README verification

---

## 🤖 Use of AI

AI was used as a **support tool** for:
- Clarifying Python syntax and type annotations
- Understanding packaging steps with `pyproject.toml`
- Checking algorithm explanations
- Improving documentation structure

AI was **not** used to replace understanding of project logic. Implementation, debugging, and algorithm integration were done as part of the development work.

---

## 📚 Resources

- [Python official documentation](https://docs.python.org/3/)
- [`random` module](https://docs.python.org/3/library/random.html)
- [`collections.deque`](https://docs.python.org/3/library/collections.html#collections.deque)
- [Packaging with `pyproject.toml`](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [flake8](https://flake8.pycqa.org/)
- [mypy](https://mypy.readthedocs.io/)