from fastapi import APIRouter, Body
from utils.command_router import handle_command

router = APIRouter()


@router.post("/chat")
def chat_endpoint(message: str = Body(..., embed=True)) -> dict:
    """
    Lightweight chat endpoint.
    If message starts with '| ' we run the command router.
    Otherwise we just echo (you can later wire this into OpenAI chat).
    """
    cmd_response = handle_command(message)
    if cmd_response is not None:
        return {"response": cmd_response}

    # Default fallback — for now just echo. Swap with GPT later.
    return {"response": f"You said: {message}"}

