import random

NAMES = [
    "Arianna", "Vladimir", "Shaddam", "Irulan", "Feyd", "Margot",
    "Alia", "Gurney", "Stilgar", "Mohiam"
]
HOUSES = [
    "Atreides", "Harkonnen", "Corrino", "Richese", "Moritani", "Ecaz"
]
ROLES = [
    "Mentat", "Swordmaster", "Reverend Mother", "Suk Doctor", "Guild Navigator", "Fremen Warrior"
]
QUIRKS = [
    "cold and unreadable", "ruthlessly ambitious", "obsessed with prophecy",
    "devoted to spice rituals", "secretly loyal to another House"
]

def generate_npc():
    """Creates a random Dune-inspired NPC."""
    name = random.choice(NAMES)
    house = random.choice(HOUSES)
    role = random.choice(ROLES)
    quirk = random.choice(QUIRKS)
    return {
        "name": name,
        "house": house,
        "role": role,
        "quirk": quirk
    }
