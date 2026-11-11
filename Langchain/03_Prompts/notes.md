Welcome to the core of LangChain! If you’ve ever built a hardcoded string like `f"Tell me a joke about {topic}"`, you already know the limitations: it gets messy fast, formatting is manual, and handling multi-turn conversations becomes a nightmare.

In LangChain, **Prompts** are treated as first-class citizens. Let’s break down every single one of these concepts step-by-step from the ground up, using simple analogies.

---

## 1. The Foundation: Prompts & Prompt Templates

### Prompts

A prompt is simply the text you send to a Large Language Model (LLM). It’s your instructions, context, and questions combined.

### Prompt Templates

Think of a **Prompt Template** as a Mad Libs sheet or a cookie cutter. Instead of writing a new string every time, you define a structure once with variables (`{variable}`) and fill them in later.

```python
from langchain_core.prompts import PromptTemplate

# 1. Define the template with a variable in curly braces
prompt_template = PromptTemplate.from_template(
    "Give me a 3-step beginner recipe for {dish} using {ingredient}."
)

# 2. Fill in the variables
formatted_prompt = prompt_template.format(dish="pasta", ingredient="garlic")
print(formatted_prompt)
# Output: Give me a 3-step beginner recipe for pasta using garlic.

```

---

## 2. Chat Prompts & The Three Message Types

Modern LLMs (like GPT-4 or Llama 3) don't just read a single block of text; they understand **conversations** broken down into specific roles. LangChain models this using distinct message classes.

### Chat Prompt Templates (`ChatPromptTemplate`)

Just like regular templates, but instead of outputting a single string, they output a **list of messages** structured for chat models.

### The Three Message Types

1. **System Messages (`SystemMessage`):** The "hidden instructions" or persona given to the model before the chat starts. It sets the rules (e.g., *"You are a strict Python coding tutor"*).
2. **Human Messages (`HumanMessage`):** What the user actually types or asks.
3. **AI Messages (`AIMessage`):** What the model previously replied with (used for maintaining conversation history).

Here is how they look together in LangChain:

```python
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant who explains concepts to a 5-year-old."),
    ("human", "Explain what {concept} is in one sentence.")
])

messages = chat_template.format_messages(concept="gravity")
print(messages)
# Output: [SystemMessage(content='You are a helpful assistant...'), HumanMessage(content='Explain what gravity is...')]

```

---

## 3. Advanced Prompting Techniques

Once you master basic templates, LangChain gives you powerful tools to handle dynamic, complex workflows.

### Few-Shot Prompting

LLMs are incredible at learning by example. **Few-Shot Prompting** means providing a few examples of input and desired output before asking the model to solve a brand-new problem.

* **How it works in LangChain:** You create a `FewShotChatMessagePromptTemplate` where you pass a list of example dictionaries and a formatting template to display them. This ensures the model mimics your exact formatting style.

### Partial Prompt Templates

Sometimes you know *some* variables ahead of time, but want to fill in others later. **Partialing** lets you "bake in" certain variables early.

```python
from langchain_core.prompts import PromptTemplate

# Template with two variables
prompt = PromptTemplate.from_template("{time_of_day}: Say hello to {name}.")

# Partial it early with 'time_of_day'
morning_prompt = prompt.partial(time_of_day="Good morning")

# Later on, just fill the remaining variable
final_prompt = morning_prompt.format(name="Alice")
print(final_prompt)
# Output: Good morning: Say hello to Alice.

```

### Dynamic Prompt Templates

What if your prompt variable isn't a static string, but a function that runs right before execution (like getting the current date, fetching a user profile, or checking the weather)?

* **How it works:** You can pass Python callables (functions) into your template values. When `.format()` or invocation runs, LangChain executes the function dynamically to grab the latest value.

### Message Placeholders (`MessagesPlaceholder`)

When building a chatbot, the conversation history grows with every turn. You can't hardcode 10 past messages into a template.

A **Message Placeholder** acts as an empty slot where you can inject a whole list of chat history dynamically at runtime.

```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful friend."),
    # This slot will accept a list of historical Human/AI messages
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{user_input}")
])

```

---

### Putting It All Together

| Tool | Purpose | When to Use |
| --- | --- | --- |
| **PromptTemplate** | Simple text templating | Standard text completion models |
| **ChatPromptTemplate** | Multi-role chat structuring | Chat models (Ollama, OpenAI chat endpoints) |
| **System/Human/AI Messages** | Defining conversation roles | Setting behavior, parsing user input & history |
| **Few-Shot Prompting** | Teaching via examples | Guiding output format or complex reasoning tasks |
| **Partial Templates** | Pre-filling variables | Reusing base templates with pre-configured settings |
| **Message Placeholders** | Injecting dynamic chat history | Building stateful chatbots |

Would you like to walk through a quick, end-to-end example of how to plug one of these chat templates into a local model runner like Ollama?