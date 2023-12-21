from fastapi import FastAPI
from chat import Chat
from chat import ChatRequest
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
chat = Chat()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

@app.post("/message/")
async def message(request: ChatRequest):
    message = request.message
    history = request.history
    cache = request.cache

    chat.enable_cache() if cache else chat.disable_cache()

    response = chat.get_message(message=message, history=history,)
    return {"message": response}