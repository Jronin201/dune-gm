# Dune TTRPG GM Tools

A modular backend system for supporting the Dune TTRPG as an AI-powered Game Master.
Built for integration with OpenAI Playground, enabling die rolls, NPC creation, and more.

## Features

- Dune 2D20 dice rolls
- Thematic NPC generation (Houses, Fremen, Guild, Bene Gesserit, etc.)
- Modular expansion for new game mechanics

## Usage

Deploy as an API backend with FastAPI. Connect endpoints to your OpenAI Playground Tools.

### `/chat` Endpoint

Send a `POST` request to `/chat` with a JSON body containing `{"message": "..."}`.
Begin the message with `|` to invoke a backend command. For example:

```bash
curl -X POST /chat -H "Content-Type: application/json" \
     -d '{"message": "| create scenario"}'
```

Commands must match exactly. Extra punctuation is ignored, so `| create scenario!` will **not** be recognized.

## Structure

- `dune-backend/src/dice.py` - FastAPI app and API routes
- `dice.py`      - Standalone dice helpers
- `chatbot-ui`   - React frontend

---

*“The beginning is a delicate time.” — Bene Gesserit Proverb*
