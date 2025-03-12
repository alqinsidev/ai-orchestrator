from fastapi import FastAPI
import uvicorn

from src.api import root, chat

app = FastAPI()

app.include_router(root.router)
app.include_router(chat.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
