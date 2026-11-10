from langchain_ollama import ChatOllama

model = ChatOllama(model="llama3.2")

response = model.invoke("What is the capital of india?")

print(response.content)

print(response)