from pathlib import Path
from fastapi import APIRouter

from utils.random_picker import load_items_from_file, pick_random_item


router = APIRouter()

DATA_DIR = Path(__file__).resolve().parents[2] / "data"
HOUSES_FILE = DATA_DIR / "houses.txt"
SETTINGS_FILE = DATA_DIR / "settings.txt"


@router.get("/random_house_setting")
def random_house_setting() -> dict:
    """Return a random house paired with a random setting."""
    houses = load_items_from_file(HOUSES_FILE)
    settings = load_items_from_file(SETTINGS_FILE)
    house = pick_random_item(houses)
    setting = pick_random_item(settings)
    return {"house": house, "setting": setting}
