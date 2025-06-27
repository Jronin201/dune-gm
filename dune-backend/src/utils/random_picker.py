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
