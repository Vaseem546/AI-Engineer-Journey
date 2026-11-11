from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_ollama import ChatOllama

messages = [
    SystemMessage(content="You are a Professional Politicina in India,Your name is Amit and you are MLA"),
    HumanMessage(content="I belong to your Constituency,my name is sunil"),
    AIMessage(content="Hello Sunil, how can I assist you today?"),
    HumanMessage(content="What is Your Name,Position and how are you going to improve your performance?")

]

model = "llama3.2"

chat_model = ChatOllama(model=model, temperature=1.5,max_tokens=25) # More temperature unique answer 
chat_model2 = ChatOllama(model=model, temperature=0.5,max_tokens=25) # Less temperature consistent answer 

response = chat_model.invoke(messages)
response2 = chat_model2.invoke(messages)

print("Response with higher temperature (1.5):")
print(response.content)

print("\nResponse with lower temperature (0.5):")
print(response2.content)