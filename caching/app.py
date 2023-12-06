from langchain.globals import set_llm_cache
from langchain.cache import RedisSemanticCache
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI

llm = OpenAI()
set_llm_cache(RedisSemanticCache(redis_url="redis://localhost:6379", embedding=OpenAIEmbeddings()))

res = llm("Tell me a joke")
print(res)
res = llm("Tell me a joke")
print(res)