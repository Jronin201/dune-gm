from openai import OpenAI
import openai
from fastapi import HTTPException

client = OpenAI()  # Uses OPENAI_API_KEY from env


def generate_adventure_text(scenario: dict) -> str:
    """Generate an adventure summary using GPT-4 based on the provided scenario."""
    scenario_text = "\n".join(f"- {k.capitalize()}: {v}" for k, v in scenario.items())

    prompt = f"""
You are a Dune storyteller tasked with creating a rich, immersive adventure summary.

Using the elements below, write a 1–2 paragraph narrative hook that could open a TTRPG session or campaign. The tone should be consistent with the lore of the Dune universe — mysterious, political, philosophical, and dangerous.

Resolve any contradictory elements creatively rather than removing them. Use Dune terminology and imagery. Avoid second-person voice.

Scenario Elements:
{scenario_text}

Begin your summary:
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a Dune campaign narrator."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.75,
        )
    except openai.OpenAIError as exc:
        # When the request fails (e.g., missing API key or network issue),
        # raise an HTTPException so the FastAPI app returns a sensible error
        raise HTTPException(status_code=503, detail=f"OpenAI API error: {exc}") from exc

    return response.choices[0].message.content.strip()
