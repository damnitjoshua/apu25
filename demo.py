from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv

load_dotenv()


async def main():
    agent = Agent(
        task="Go to https://www.google.com/maps and search for cafes near me. Extract the list of cafe names and their addresses. Return the result as a JSON array with objects containing 'name' and 'address'.",
        llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash"),
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
