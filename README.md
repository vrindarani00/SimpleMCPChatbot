````markdown

SimpleMCPChatbot
 ![background](https://github.com/user-attachments/assets/90915101-6867-4de5-b0b8-33a8e6fb42a3)


This repo contains a basic chatbot using multiple MCP servers connecting via the Model Context Protocol (MCP).

**LLM used:**  
**Qwen-QwQ-32B** is a medium-sized, open-source reasoning model developed by the Qwen team (Alibaba), designed specifically for complex problem-solving and logical reasoning tasks. Unlike general-purpose language models that excel at conversational fluency, QwQ-32B is optimized for structured, multi-step reasoning, making it particularly effective for technical domains such as mathematics, coding, scientific research, and finance.

---

## MCP servers used

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest"
      ]
    },
    "airbnb": {
      "command": "npx",
      "args": [
        "-y",
        "@openbnb/mcp-server-airbnb"
      ]
    },
    "duckduckgo-search": {
      "command": "npx",
      "args": [
        "-y",
        "duckduckgo-mcp-server"
      ]
    }
  }
}
````

---

## Basic Flow

1. **Configure servers**
   Create a JSON file (`browsermcp.json`) listing all your MCP servers.
2. **Initialize client & LLM**

   ```python
   client = MCPClient.from_config('browsermcp.json')
   llm    = ChatGroq(model="qwen-qwq-32b")
   agent  = MCPAgent(
       llm=llm,
       client=client,
       verbose=True,
       max_turns=10,
       max_tokens=1000,
       temperature=0.7,
       memory_enabled=True,
   )
   ```
3. **Interactive loop**

   ```python
   while True:
       user_input = input("You: ")
       if user_input.lower() == "exit":
           break
       if user_input.lower() == "clear":
           agent.clear_memory()
           continue
       response = await agent.invoke(user_input)
       print(f"MCP: {response}")
   ```
4. **Cleanup**

   ```python
   await client.close_all_sessions()
   ```

---

## Requirements

* **Python ≥3.11**
* **Node.js**

**`pyproject.toml`** snippet:

```toml
[project]
name = "chatbot-mcp-version"
version = "0.1.0"
description = "A simple multi-server MCP chatbot demo"
readme = "README.md"
requires-python = ">=3.11"

dependencies = [
    "langchain-groq>=0.3.2",
    "langchain-openai>=0.3.17",
    "mcp-use>=1.2.13",
]
```
