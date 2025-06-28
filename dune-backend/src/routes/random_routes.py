from pathlib import Path
from fastapi import APIRouter

# Required for deployment on Render: import from local ``utils`` package
from src.utils.random_picker import pick_random_item_from_file
from src.utils.scenario_utils import generate_adventure_text


router = APIRouter()

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


@router.get("/random_scenario")
def get_random_scenario() -> dict:
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


@router.post("/generate_adventure")
def generate_adventure(scenario: dict) -> dict:
    """Return GPT-generated adventure text for the given scenario."""
    adventure_text = generate_adventure_text(scenario)
    return {"adventure_text": adventure_text}
