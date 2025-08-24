from my_agents.hotel_assistant import get_hotel_agent
from agents import Runner
import asyncio


async def main():
    # Choose which hotel agent to use
    hotel_name = "Hotel Green Valley"
    agent = get_hotel_agent(hotel_name)

    query = "How many rooms are available in the hotel?"
    result = await Runner.run(agent, query)
    print(result.final_output)


asyncio.run(main())


