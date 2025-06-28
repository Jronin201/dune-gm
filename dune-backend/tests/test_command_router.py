from pathlib import Path
import sys

# Allow imports from dune-backend/src
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.utils.command_router import handle_command

HEADER = "**Random Dune Scenario Elements**"

def test_non_command_returns_none():
    assert handle_command("hello") is None

def test_create_scenario_synonym_parses():
    result = handle_command("| create scenario please!")
    assert result.startswith(HEADER)

def test_punctuation_stripped():
    result = handle_command("| create scenario?!")
    assert result.startswith(HEADER)
