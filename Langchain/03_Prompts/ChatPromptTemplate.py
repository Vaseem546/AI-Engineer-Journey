from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

chat_prompts = ChatPromptTemplate.from_messages([
    ("system", "You are a Sarcatic Standup Comedian"),
    ("human", "Tell me a joke about {topic} in India")
])

chat_model = ChatOllama(model="llama3.2",
                        temperature=1.5)

formatted_messages = chat_prompts.format_messages(topic="politics")
print(formatted_messages)

response = chat_model.invoke(formatted_messages)
print(response.content)


