from typing import Dict


def parse_config(filename: str) -> Dict[str, str]:
    config: Dict[str, str] = {}

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            key, value = line.split("=")
            config[key] = value

    return config


def parse_entry(value: str) -> tuple[int, int]:
    x_str, y_str = value.split(",")
    return int(x_str), int(y_str)


def load_config(filename: str) -> dict:
    raw = parse_config(filename)

    config = {
        "width": int(raw["WIDTH"]),
        "height": int(raw["HEIGHT"]),
        "entry": parse_entry(raw["ENTRY"]),
        "exit": parse_entry(raw["EXIT"]),
        "perfect": raw.get("PERFECT", "True") == "True",
        "seed": int(raw.get("SEED", "0")),
    }

    return config
