from langchain_ollama import ChatOllama

model = ChatOllama(model="llama3.2")

# A list of independent prompts
prompts = [
    "What is the capital of France? Answer in one word.",
    "What is the capital of Japan? Answer in one word.",
    "What is the capital of Australia? Answer in one word."
]

print("Processing batch requests...")
results = model.batch(prompts)

for i, res in enumerate(results):
    print(f"Prompt {i+1} Response: {res.content}")