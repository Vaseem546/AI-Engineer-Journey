from langchain_ollama import ChatOllama
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.messages import HumanMessage

chat_model = ChatOllama(model="llama3.2")


response_schemas = [
    ResponseSchema(
        name="summary" , description="A one line suummary of the topic"
    ),
    ResponseSchema(
        name="difficulty" , description = "Diffiulty level: Easy,Medium,Hard"
    )
]


parser = StructuredOutputParser.from_response_schemas(response_schemas)
foramt_instructions = parser.get_format_instructions()

prompt = f"Analyze the asynchronous programming.{foramt_instructions}"

result = chat_model.invoke([HumanMessage(content=prompt)])
parsed_output = parser.parse(result.content)

print(parsed_output)