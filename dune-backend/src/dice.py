"""Minimal FastAPI app providing simple D20 dice rolls."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

# src/dice.py  (top of file)

from src.routes.random_routes import router as random_router
from src.routes.chat_routes import router as chat_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(random_router)
app.include_router(chat_router)


@app.get("/")
def root():
    """Simple index confirming the API is running."""
    return {"welcome": "Dune dice API online"}


def _roll_d20(num: int) -> list[int]:
    """Return a list with ``num`` rolls of a 20-sided die."""
    return [random.randint(1, 20) for _ in range(num)]


def roll_1d20() -> dict:
    """Roll a single 20-sided die."""
    result = _roll_d20(1)[0]
    return {"result": result}


def roll_2d20() -> dict:
    """Roll two 20-sided dice."""
    results = _roll_d20(2)
    return {"results": results}


@app.get("/roll/1d20")
def api_roll_1d20() -> dict:
    """API endpoint that returns the result of :func:`roll_1d20`."""
    return roll_1d20()


@app.get("/roll/2d20")
def api_roll_2d20() -> dict:
    """API endpoint that returns the results of :func:`roll_2d20`."""
    return roll_2d20()
