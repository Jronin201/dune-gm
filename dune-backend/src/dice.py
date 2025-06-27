"""Minimal FastAPI app providing simple D20 dice rolls."""

from fastapi import FastAPI
import random

# Required for deployment on Render: the app is executed from within ``src``
# so we import routes as local packages instead of using the ``src`` prefix.
from routes.random_routes import router as random_router

app = FastAPI()
app.include_router(random_router)


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
