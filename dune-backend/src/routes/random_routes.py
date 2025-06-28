from pathlib import Path
from fastapi import APIRouter

# Required for deployment on Render: import from local ``utils`` package
from src.utils.random_picker import get_random_scenario
from src.utils.scenario_utils import generate_adventure_text
from src.utils.command_router import cmd_test


router = APIRouter()

# ---------------------------------------------------------------------------
#  Data-file locations (still used by get_random_scenario)
# ---------------------------------------------------------------------------
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

# ---------------------------------------------------------------------------
#  Simple helpers
# ---------------------------------------------------------------------------


@router.get("/random_scenario")
def random_scenario() -> dict:
    """Return a randomly generated scenario (legacy path)."""
    return get_random_scenario()

# ---------------------------------------------------------------------------
#  NEW: GET endpoint that Chatbot-UI calls for | Create Scenario
# ---------------------------------------------------------------------------


@router.get("/scenario_elements")
def quick_scenario() -> dict:
    """Return random scenario elements plus a follow-up prompt."""
    scenario = get_random_scenario()
    return {
        "scenario": scenario,
        "prompt": "Would you like me to craft these elements into a powerful scenario?"
    }

# ---------------------------------------------------------------------------
#  POST / GET variants that deliver raw elements (kept for API compatibility)
# ---------------------------------------------------------------------------


@router.post("/generate_scenario")
def generate_scenario(scenario: dict | None = None) -> dict:
    """Return elements (or supplied dict) with prompt."""
    if not scenario:                      # None *or* {}
        scenario = get_random_scenario()

    return {
        "scenario": scenario,
        "prompt": "Would you like me to craft these elements into a powerful scenario?",
    }


@router.post("/generate_adventure")
def generate_adventure(scenario: dict) -> dict:
    """Return GPT-generated adventure text for the given scenario."""
    adventure_text = generate_adventure_text(scenario)
    return {"adventure_text": adventure_text}
