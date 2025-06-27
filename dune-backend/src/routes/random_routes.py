from pathlib import Path
from fastapi import APIRouter

# Required for deployment on Render: import from local ``utils`` package
from src.utils.random_picker import pick_random_item, load_items_from_file


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
