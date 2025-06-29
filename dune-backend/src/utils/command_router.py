"""Utility functions to parse and execute in-chat commands that start with '| '."""

import os
import requests
from src.utils.random_picker import get_random_scenario


def cmd_create_scenario() -> str:
    """Generate random scenario elements and return a nicely formatted string."""
    s = get_random_scenario()
    lines = [
        "**Random Dune Scenario Elements**",
        f"- **House:** {s['house']}",
        f"- **Setting:** {s['setting']}",
        f"- **Objective:** {s['objective']}",
        f"- **Antagonist:** {s['antagonist']}",
        f"- **Twist:** {s['twist']}",
        f"- **Ally:** {s['ally']}",
        f"- **Environment:** {s['environment']}",
        f"- **Artifact:** {s['artifact']}",
        f"- **Mystical:** {s['mystical']}",
        f"- **Consequence:** {s['consequence']}",
        "",
        "*Would you like me to craft these elements into a powerful scenario?*"
    ]
    return "\n".join(lines)


def cmd_scenario_story() -> str:
    """Call the backend /scenario_story endpoint and return its text."""
    base = os.getenv("BACKEND_URL", "http://localhost:8000")
    r = requests.get(f"{base}/scenario_story", timeout=30)
    r.raise_for_status()
    return r.json()["response"]


def cmd_test() -> str:
    """Return a confirmation that the command system works."""
    return "Test Satisfactory"


COMMAND_MAP = {
    "create scenario": cmd_create_scenario,
    "scenario story":  cmd_scenario_story,
    "test": cmd_test,
}


def handle_command(raw: str) -> str | None:
    """If *raw* begins with '| ', parse the command and execute.
    Otherwise return None."""
    if not raw.lstrip().startswith("|"):
        return None

    cmd = raw.lstrip()[1:].strip().lower()          # drop leading '|'
    cmd = cmd.rstrip('!?.,')                        # drop trailing punctuation
    cmd_key = " ".join(cmd.split()[:2])            # first two words for synonyms
    fn = COMMAND_MAP.get(cmd) or COMMAND_MAP.get(cmd_key)
    if fn:
        return fn()
    return f"Unrecognized command: `{cmd}`"

