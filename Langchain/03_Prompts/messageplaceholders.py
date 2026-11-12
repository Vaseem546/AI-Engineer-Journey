from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama


chat_model = ChatOllama(model="llama3.2")

messages = ChatPromptTemplate.from_messages([
    ("system","You are ahelpful chatbot"),
    MessagesPlaceholder(variable_name="history"),
    ("human","{question}")
])

past_messages = [
    HumanMessage(content="My Secret number is 22")
]

prompt= messages.format_messages(
    history=past_messages,question="What is my secret number"
)

response= chat_model.invoke(prompt)
print(response.content)