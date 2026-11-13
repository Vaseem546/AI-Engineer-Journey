from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage

chat_model = ChatOllama(model ="llama3.2",temperature=0.5)

messages = [HumanMessage(content="Tell me a joke in 2 lines")]

response = chat_model.invoke(messages)

parser = StrOutputParser()

clean_response = parser.invoke(response)

#print(response)
print(clean_response)