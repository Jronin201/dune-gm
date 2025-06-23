# Dune TTRPG GM Tools

A modular backend system for supporting the Dune TTRPG as an AI-powered Game Master.
Built for integration with OpenAI Playground, enabling die rolls, NPC creation, and more.

## Features

- Dune 2D20 dice rolls
- Thematic NPC generation (Houses, Fremen, Guild, Bene Gesserit, etc.)
- Modular expansion for new game mechanics

## Usage

Deploy as an API backend with FastAPI. Connect endpoints to your OpenAI Playground Tools.

## Structure

- `app.py`       - FastAPI entrypoint, routes
- `dice.py`      - Dice rolling mechanics
- `npc.py`       - NPC generation logic

---

*“The beginning is a delicate time.” — Bene Gesserit Proverb*
