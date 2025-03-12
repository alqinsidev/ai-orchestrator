from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from typing import AsyncGenerator

from src.graph.workflow import graph
from src.state.chat_state import create_chat_state
from src.llm.gemini import GeminiModule


router = APIRouter()


async def stream_response(prompt: str) -> AsyncGenerator[str, None]:
    model = GeminiModule()
    for chunk in model.stream_generate(prompt=prompt):
        yield chunk


@router.get("/chat")
async def chat(query: str):
    state = create_chat_state(query)
    state = graph.invoke(state)
    prompt = (
        f"User Query: {state['user_query']}\n\n"
        f"SQL Agent Response: {state['sql_response']}\n"
        f"Berikan jawaban berdasarkan konteks tersebut"
    )
    return StreamingResponse(
        stream_response(prompt),
        media_type="text/event-stream",
    )
