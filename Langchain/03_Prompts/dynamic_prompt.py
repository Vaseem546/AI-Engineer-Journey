from datetime import datetime
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama


def get_date_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are are atiming asssistant that tells time and date with this timing {timeanddate}"),
    ("human","Tell current time with the instructions you have got")
])

format_prompt = prompt_template.format_messages(timeanddate=get_date_time())

chat_model = ChatOllama(model="llama3.2")

response = chat_model.invoke(format_prompt)

print(response.content)