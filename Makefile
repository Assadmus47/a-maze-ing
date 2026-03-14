
PYTHON = python3
MAIN = a_maze_ing.py

run:
	$(PYTHON) $(MAIN) config.txt

debug:
	$(PYTHON) -m pdb $(MAIN)

install:
	$(PYTHON) -m pip install flake8 mypy

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	flake8 .
	mypy . --strict

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".mypy_cache" -exec rm -rf {} +

.PHONY: run debug install lint lint-strict clean