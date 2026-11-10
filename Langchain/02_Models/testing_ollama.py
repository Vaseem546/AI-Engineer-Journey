from langchain_ollama import ChatOllama

model = ChatOllama(model="llama3.2")

response = model.invoke("What is the capital of USA?")

print(response.content)

print(response)