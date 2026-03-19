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

You can run the project in two ways:

```bash
# Using the main Python file
python3 a_maze_ing.py

# Or using the installed entry point
mazegen
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
WIDTH=10
HEIGHT=8
ENTRY=0,0
EXIT=9,7
PERFECT=True
SEED=8
```

### Parameters

| Key | Type | Required | Description |
|---|---|---|---|
| `WIDTH` | integer | ✅ | Number of columns (strictly positive) |
| `HEIGHT` | integer | ✅ | Number of rows (strictly positive) |
| `ENTRY` | `x,y` | ✅ | Entry point coordinates (must be inside the grid) |
| `EXIT` | `x,y` | ✅ | Exit point coordinates (must differ from ENTRY) |
| `PERFECT` | boolean | ✅ | If `True`, exactly one path exists between any two cells |
| `SEED` | integer | ✅ | Initializes the RNG for deterministic generation |

### Parsing & Validation

The parser:
- Reads the file line by line and splits on `=`
- Converts values to their expected types
- Validates all constraints

Invalid configurations (e.g. `WIDTH=abc`, `ENTRY=100,100`, missing keys) are rejected with a clear error message.

---

## 🏗️ Maze Generation — DFS with Backtracking

The algorithm starts from an initial cell and explores by always moving to an unvisited neighbor. When stuck, it backtracks using a stack.

```python
random.seed(seed)
stack = [start]
visited = {start}

while stack:
    current = stack[-1]
    neighbors = get_unvisited_neighbors(current)
    if neighbors:
        next_cell = random.choice(neighbors)
        remove_wall(current, next_cell)
        visited.add(next_cell)
        stack.append(next_cell)
    else:
        stack.pop()  # backtrack
```

**Why DFS?** Simple, efficient on grids, produces interesting mazes, and naturally demonstrates stacks, backtracking, and random neighbor selection.

---

## 🔍 Maze Solving — BFS (Shortest Path)

BFS explores the maze level by level, guaranteeing the **shortest path** from entry to exit.

```python
queue = deque([start])
visited = {start}
came_from = {}

# Path reconstruction
current = goal
while current != start:
    current = came_from[current]
    path.append(current)
path.reverse()
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

### Anticipated planning and how it evolved

The initial plan was sequential:

1. Define the project structure
2. Implement config parsing
3. Implement the maze grid
4. Implement maze generation
5. Implement maze solving
6. Implement terminal display
7. Implement output export
8. Write documentation and package the project

In practice, the planning became **more iterative** than linear. Some tasks required more back-and-forth than expected, especially the internal wall representation, keeping display logic readable, path storage for both export and display, and packaging with `pyproject.toml`.

### What worked well

- Clear separation between parsing, generation, solving, display, and output
- A grid representation that stayed efficient throughout
- Using DFS for generation and BFS for solving was a natural and complementary pairing
- Progressive testing while building each feature avoided large integration bugs

### What could be improved

- More automated tests from the start
- Cleaner abstraction between display and maze internals
- A more formal package structure defined earlier in the project
- Writing the README earlier to avoid documentation debt at the end

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
