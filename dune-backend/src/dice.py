from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/")
def root():
    """Simple index confirming the API is running."""
    return {"welcome": "Dune dice API online"}


def roll_1d20():
    """Rolls a single 20-sided die."""
    result = random.randint(1, 20)
    return {"result": result}


def roll_2d20():
    """Rolls two 20-sided dice."""
    results = [random.randint(1, 20), random.randint(1, 20)]
    return {"results": results}


@app.get("/roll/1d20")
def api_roll_1d20():
    return roll_1d20()


@app.get("/roll/2d20")
def api_roll_2d20():
    return roll_2d20()
