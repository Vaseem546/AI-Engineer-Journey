from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

prompt_template = PromptTemplate.from_template(
    "Write a {tone} explanation about {topic}."
)

partial_prompt = prompt_template.partial(tone="humorous")

final_prompt = partial_prompt.format(topic="black holes")

print(final_prompt)

chat_model = ChatOllama(model="llama3.2",
                        temperature=0.8,
                        max_tokens=20)
response= chat_model.invoke(final_prompt)
print(response.content)