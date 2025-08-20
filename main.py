from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import asyncio
import os


load_dotenv()

model = ChatGoogleGenerativeAI(
     model="gemini-2.5-pro",
     temperature=0.0,
     google_api_key=os.getenv("GOOGLE_API_KEY")
)

server_params = StdioServerParameters(
    command="npx",
    env={
        "FIRECRAWL_API_KEY": os.getenv("FIRECRAWL_API_KEY"),
    },
    args=['firecrawl-mcp']
)

async def main():
    async with stdio_client(server_params) as (read , write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            agent = create_react_agent(model, tools)


            messages = [
                {

                    "role": "system",
                    "content": "You are a powerful web research assistant. Your primary function is to answer questions by using the tools provided."
                        "DO NOT mention that you cannot access the internet. Your tools give you that capability."
                        "Always follow this process:"
                        "1. Think about the user's request."
                        "2. If the request requires information you don't have, decide which tool is best for the job."
                        "3. Use the tool to find the information."
                        "4. Analyze the tool's output and answer the user's question based on the data you found."
                        "\nFor example, if a user asks 'what are the top 5 headphones on amazon', you should use the 'firecrawl_search' tool with a query like 'top 5 headphones on amazon.com'."
                }
            ]

            print("Available Tools -", *[tool.name for tool in tools])
            print('-' * 60)


            while True:
                user_input = input("\nYou:")
                if user_input == "quit":
                    print("Goodbye")
                    break


                messages.append({"role": "user", "content": user_input[:175000]})


                try:
                    agent_response = await agent.ainvoke({"messages": messages})

                    ai_message = agent_response["messages"] [-1].content
                    print("\nAgent: ", ai_message)
                except Exception as e:
                    print('Error', e)


if __name__ == "__main__":
    asyncio.run(main())












