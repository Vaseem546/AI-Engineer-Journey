from langchain_ollama import ChatOllama

model ="llama3.2"

#Created a accurate model with the temperature 0.5 that gives predictable answers
accurate_model = ChatOllama(model=model,
                   temperature=0.5,
                   max_tokens=30)

#Created a creative model with the temperature 1.5 that gives more creative answers
creative_model = ChatOllama(model=model,
                            temperature=1.5,
                            max_tokens=30)

prompt="Write a creative opening sentence for a horror story happened in indian city."

print("Accurate Model Response:")
print(accurate_model.invoke(prompt).content)

print("Creative Model Response:")
print(creative_model.invoke(prompt).content)


