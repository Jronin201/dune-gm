from fastapi import FastAPI
from dice import roll_1d20, roll_2d20
from npc import generate_npc

app = FastAPI()

@app.get("/")
def root():
    return {"welcome": "Dune TTRPG GM Tools - API is live."}

@app.get("/roll/1d20")
def api_roll_1d20():
    return roll_1d20()

@app.get("/roll/2d20")
def api_roll_2d20():
    return roll_2d20()

@app.get("/npc")
def api_generate_npc():
    return generate_npc()
