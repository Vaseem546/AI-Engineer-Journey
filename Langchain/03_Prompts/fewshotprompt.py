from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_ollama import ChatOllama

examples = [
    {"input":"Happy","output":"Sad"},
    {"input":"Tall","output":"Short"},
    {"input":"Hot","output":"Cold"}
]

prompt_structure = ChatPromptTemplate.from_messages([
    ("human","{input}"),("ai","{output}")
])

few_shot_prompt = FewShotChatMessagePromptTemplate(
    examples=examples,
    example_prompt=prompt_structure
)

actual_prompt = ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant that provides antonyms for given words in single word."),
    few_shot_prompt,
    ("human","{input}")
])

chat_model = ChatOllama(model="llama3.2")

response= chat_model.invoke(actual_prompt.format_messages(input="Beautiful"))

print(response.content)