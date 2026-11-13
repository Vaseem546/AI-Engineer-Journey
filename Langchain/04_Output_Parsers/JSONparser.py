from langchain_ollama import ChatOllama
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.messages import HumanMessage

chat_model = ChatOllama(model="llama3.2")

parser = JsonOutputParser()

prompt = f"Give me a fruit and its colour.{parser.get_format_instructions()}"

response = chat_model.invoke([HumanMessage(content=prompt)])

json_response = parser.invoke(response)

print(response.content)
print(json_response)


#Accessing like a normal dictioary from a LLM Response
print(json_response["fruit"])