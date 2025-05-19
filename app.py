import os
import asyncio
from dotenv import load_dotenv
from mcp_use import MCPAgent, MCPClient
from langchain_groq import ChatGroq

async def run_mem_chat():
    # Load environment and init client/agent
    load_dotenv()
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    print("Initializing MCP client…")
    client = MCPClient.from_config('browsermcp.json')
    llm = ChatGroq(model="qwen-qwq-32b")
    agent = MCPAgent(
        llm=llm,
        client=client,
        verbose=True,
        max_turns=10,
        max_tokens=1000,
        temperature=0.7,
        memory_enabled=True,
    )

    print("\n==== Interactive MCP chatbot ====")
    print("Type 'exit' to end the conversation")
    print("Type 'clear' to clear the memory")

    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Exiting the conversation…")
                break

            if user_input.lower() == "clear":
                agent.clear_memory()
                print("Memory cleared")
                continue

            response = await agent.invoke(user_input)
            print(f"MCP: {response}")

    finally:
        # Clean up when loop exits (either via break or error)
        if client and getattr(client, "sessions", None):
            await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(run_mem_chat())
