from agents import Agent
from my_config.gemini_config import MODEL
from guardrail_function.guardrail_function import guardrial_input_function


# -----------------------
# Hotel Data Store
# -----------------------
HOTELS = {
    "Hotel Royal Orchid": {
        "rooms": 200,
        "reserved_rooms": 20,
        "owner": "Mr. Salman Khan",
    },
    "Hotel Green Valley": {
        "rooms": 150,
        "reserved_rooms": 10,
        "owner": "Ms. Ayesha Khan",
    },
    "Hotel Ocean View": {
        "rooms": 300,
        "reserved_rooms": 50,
        "owner": "Mr. John Smith",
    },
}


def build_instructions(hotel_name: str) -> str:
    """
    Dynamically build instructions for a given hotel.
    """
    if hotel_name not in HOTELS:
        return f"You are a helpful hotel assistant. But note: Hotel '{hotel_name}' is not in the database."

    hotel = HOTELS[hotel_name]
    return f"""
    You are a helpful hotel customer care assistant.

    - Hotel name is {hotel_name}.
    - Hotel owner name is {hotel['owner']}.
    - Hotel total rooms: {hotel['rooms']}.
    - {hotel['reserved_rooms']} rooms not available for public (reserved for special guests).
    """


# -----------------------
# Dynamic Agent Factory
# -----------------------
def get_hotel_agent(hotel_name: str) -> Agent:
    """
    Create an agent dynamically for the requested hotel.
    """
    return Agent(
        name=f"{hotel_name} Customer Care",
        instructions=build_instructions(hotel_name),
        model=MODEL,
        input_guardrails=[guardrial_input_function],
        output_guardrails=[],
    )
