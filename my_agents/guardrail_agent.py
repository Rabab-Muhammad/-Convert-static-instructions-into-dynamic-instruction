from agents import Agent
from my_config.gemini_config import MODEL
from data_schema.my_date_schema import MyDataType

guardrail_agent = Agent(
    name="Guradrial Agent for Hotel Green Valley",
    instructions="Check queries for hotel Green Valley",
    model=MODEL,
    output_type=MyDataType

)