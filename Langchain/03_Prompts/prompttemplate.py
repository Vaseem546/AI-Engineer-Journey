from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

prompt_template = PromptTemplate.from_template(
    "Write a {topic} in a {emotion} tone in 5 lines."

)

prompt = prompt_template.format(topic="poem",emotion="angry")

chat_model = ChatOllama(model="llama3.2",
                        temperature=0.8)

response = chat_model.invoke(prompt)
print(response.content)