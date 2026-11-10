from langchain_ollama import ChatOllama
import asyncio   #To implemeted async and await using aincoke and astream we have to sue this to run the async fucntions as python does not do it normally

model = "llama3.2"

chat_model = ChatOllama(model=model)

async def main1():
    prompt = "What is the capital of India?"
    response = await chat_model.ainvoke(prompt)
    print("Async Invoke Response:")
    print(response.content)


async def main2():
    prompt ="What are the names of planets list any 2"
    async for chunk in chat_model.astream(prompt):
        print(chunk.content,end="",flush=True)


async def allrun():
    await main1()
    await main2()

asyncio.run(allrun())
