from langchain_ollama import ChatOllama

model = "llama3.2"

chat_model = ChatOllama(model=model,
                       temperature=0.5)

prompt = "What are the names of the planets in our solar system?"

#This will invoke the model and get the response when we run the script the model will 
# get all the names of planet at once and retrun the output in one go.
print("Invoke Response Thinking")
response_invoke = chat_model.invoke(prompt)
print(response_invoke.content)

#For loop is used to define the functionality of stream method 
# which will give the output in chunks and print the output in real time.
for chunk in chat_model.stream(prompt):
    print(chunk.content, end="",flush=True)



