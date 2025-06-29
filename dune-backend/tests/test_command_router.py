from pathlib import Path
import sys

# Allow imports from dune-backend/src
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.utils import command_router
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


def test_test_command():
    assert handle_command("| test") == "Test Satisfactory"


def test_scenario_story_command(monkeypatch):
    """Ensure the scenario story command calls the backend and returns text."""

    class DummyResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return {"response": "dummy story"}

    def fake_get(url, timeout=30):
        assert url.endswith("/scenario_story")
        return DummyResponse()

    monkeypatch.setattr(command_router.requests, "get", fake_get)

    result = handle_command("| scenario story")
    assert result == "dummy story"
