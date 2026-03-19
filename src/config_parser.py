from typing import Dict


def parse_entry(value: str) -> tuple[int, int]:
    x_str, y_str = value.split(",")
    return int(x_str), int(y_str)


def validate_config(raw: dict) -> dict:

    required = ["WIDTH", "HEIGHT", "ENTRY", "EXIT", "PERFECT"]

    for key in required:
        if key not in raw:
            raise ValueError(f"Missing key: {key}")

    try:
        width = int(raw["WIDTH"])
        height = int(raw["HEIGHT"])
    except ValueError:
        raise ValueError("WIDTH and HEIGHT must be integers")

    if width <= 0 or height <= 0:
        raise ValueError("WIDTH and HEIGHT must be > 0")

    if width < 9 or height < 7:
        raise ValueError("Maze must be at least 9x7")

    try:
        entry = parse_entry(raw["ENTRY"])
        exit_ = parse_entry(raw["EXIT"])
    except Exception:
        raise ValueError("ENTRY and EXIT must be x,y")

    for x, y in [entry, exit_]:
        if not (0 <= x < width and 0 <= y < height):
            raise ValueError("ENTRY/EXIT out of bounds")

    if entry == exit_:
        raise ValueError("ENTRY and EXIT must be different")

    perfect_str = raw["PERFECT"]
    if perfect_str not in ["True", "False"]:
        raise ValueError("PERFECT must be True or False")

    perfect = perfect_str == "True"

    try:
        seed = int(raw.get("SEED", "0"))
    except ValueError:
        raise ValueError("SEED must be an integer")

    output_file = raw.get("OUTPUT_FILE", "maze_output.txt")

    return {
        "width": width,
        "height": height,
        "entry": entry,
        "exit": exit_,
        "perfect": perfect,
        "seed": seed,
        "output_file": output_file,
    }


def parse_config(filename: str) -> Dict[str, str]:
    config: Dict[str, str] = {}

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if "=" not in line:
                raise ValueError(f"Invalid line: {line}")

            key, value = line.split("=", 1)
            config[key] = value

    return config


def load_config(filename: str) -> dict:
    raw = parse_config(filename)

    return validate_config(raw)
