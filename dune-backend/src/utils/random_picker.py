from pathlib import Path
import random
from typing import Sequence


def load_items_from_file(path: Path) -> list[str]:
    """Load non-blank lines from ``path`` and return them as a list."""
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def pick_random_item(items: Sequence[str]) -> str:
    """Return a random element from ``items``."""
    if not items:
        raise ValueError("No items to choose from")
    return random.choice(list(items))


def pick_random_item_from_file(path: Path) -> str:
    """Return a random non-blank line from ``path``."""
    items = load_items_from_file(path)
    return pick_random_item(items)


DATA_DIR = Path(__file__).resolve().parents[2] / "data"
HOUSES_FILE = DATA_DIR / "houses.txt"
SETTINGS_FILE = DATA_DIR / "settings.txt"
OBJECTIVES_FILE = DATA_DIR / "objectives.txt"
ANTAGONISTS_FILE = DATA_DIR / "antagonists.txt"
TWISTS_FILE = DATA_DIR / "twists.txt"
ALLIES_FILE = DATA_DIR / "allies.txt"
ENVIRONMENT_FILE = DATA_DIR / "environment.txt"
ARTIFACTS_FILE = DATA_DIR / "artifacts.txt"
MYSTICISM_FILE = DATA_DIR / "mysticism.txt"
CONSEQUENCES_FILE = DATA_DIR / "consequences.txt"


def get_random_scenario() -> dict[str, str]:
    """Return a randomly generated scenario pulling one item from each data file."""
    return {
        "house": pick_random_item_from_file(HOUSES_FILE),
        "setting": pick_random_item_from_file(SETTINGS_FILE),
        "objective": pick_random_item_from_file(OBJECTIVES_FILE),
        "antagonist": pick_random_item_from_file(ANTAGONISTS_FILE),
        "twist": pick_random_item_from_file(TWISTS_FILE),
        "ally": pick_random_item_from_file(ALLIES_FILE),
        "environment": pick_random_item_from_file(ENVIRONMENT_FILE),
        "artifact": pick_random_item_from_file(ARTIFACTS_FILE),
        "mystical": pick_random_item_from_file(MYSTICISM_FILE),
        "consequence": pick_random_item_from_file(CONSEQUENCES_FILE),
    }
