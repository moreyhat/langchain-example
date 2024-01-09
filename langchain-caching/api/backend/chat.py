from typing import List
from pydantic import BaseModel
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.globals import set_llm_cache
from langchain.cache import RedisSemanticCache
from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
import os

HUGGING_FACE_API_KEY = os.environ["HUGGING_FACE_API_KEY"]

embedding = HuggingFaceInferenceAPIEmbeddings(
    api_key=HUGGING_FACE_API_KEY,
    model_name="pkshatech/GLuCoSE-base-ja",
)

cache_db = RedisSemanticCache(
    redis_url="redis://cache:6379",
    embedding=embedding,
    score_threshold=0.005,
)

set_llm_cache(cache_db)


class ConversationMessage(BaseModel):
    type: str
    content: str


class ChatRequest(BaseModel):
    message: str
    history: List[ConversationMessage] = []
    cache: bool = False


class Chat:
    def __init__(self) -> None:
        self.client = ChatOpenAI(cache=False)

    def enable_cache(self):
        self.client.cache = True

    def disable_cache(self):
        self.client.cache = False

    def get_message(self, message: str, history: List[ConversationMessage] = []) -> str:
        messages = []
        for conversation_msg in history:
            if conversation_msg.type == "AI":
                messages.append(SystemMessage(content=conversation_msg.content))
            else:
                messages.append(HumanMessage(content=conversation_msg.content))

        messages.append(HumanMessage(content=message))
        response = self.client(messages)

        return response.content
