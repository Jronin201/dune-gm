from fastapi import APIRouter, Body
from src.utils.command_router import handle_command

router = APIRouter()


@router.post("/chat")
def chat_endpoint(message: str = Body(..., embed=True)) -> dict:
    """
    Chat entrypoint. If the message begins with '| ', execute a backend command;
    otherwise, just echo (placeholder for future GPT chat).
    """
    cmd_response = handle_command(message)
    if cmd_response is not None:
        return {"response": cmd_response}

    return {"response": f"You said: {message}"}
