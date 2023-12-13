from langchain.globals import set_llm_cache
from langchain.cache import RedisSemanticCache
from langchain.memory import ConversationBufferMemory
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from operator import itemgetter


set_llm_cache(RedisSemanticCache(redis_url="redis://localhost:6379", embedding=OpenAIEmbeddings()))

llm = ChatOpenAI()
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful chatbot"),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)

memory = ConversationBufferMemory(return_messages=True)
memory.load_memory_variables({})

chain = (
    RunnablePassthrough.assign(
        history=RunnableLambda(memory.load_memory_variables) | itemgetter("history")
    )
    | prompt
    | llm
)

inputs = {"input": "Hi I'm bob"}
response = chain.invoke(inputs)

memory.save_context(inputs, {"output": response.content})
print(memory.load_memory_variables({}))

inputs = {"input": "Whats my name"}
response = chain.invoke(inputs)
print(response.content)

print(response.content)