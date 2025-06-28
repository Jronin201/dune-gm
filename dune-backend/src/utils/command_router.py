"""Utility functions to parse and execute in-chat commands that start with '| '."""

from utils.random_picker import get_random_scenario


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


COMMAND_MAP = {
    "create scenario": cmd_create_scenario
}


def handle_command(raw: str) -> str | None:
    """If *raw* begins with '| ', parse the command and execute.
    Otherwise return None."""
    if not raw.lstrip().startswith("|"):
        return None

    cmd = raw.lstrip()[1:].strip().lower()          # drop leading '|'
    fn = COMMAND_MAP.get(cmd)
    if fn:
        return fn()
    return f"Unrecognized command: `{cmd}`"

