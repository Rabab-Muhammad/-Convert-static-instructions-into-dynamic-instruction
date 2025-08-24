## 🏨 Hotel Assistant Agent - Assignment 9
This project demonstrates how to convert static instructions into dynamic ones using OpenAI’s Agent SDK.
The system manages multiple hotels and allows users to query hotel details dynamically.

## 🎯 Objective
 - Convert static hotel assistant into a dynamic agent system.
 - Support multiple hotels from a single agent factory.
 - Use guardrails to validate and restrict queries (e.g., ensure queries are about the correct hotel).

## 📂 Project Structure
```graphql
project/
│── my_agents/
│   ├── hotel_assistant.py   # Dynamic agent factory + hotel data
│   ├── guardrail_agent.py   # Guardrail agent definition
│
│── guardrail_function/
│   ├── guardrail_function.py # Input guardrail logic
│
│── data_schema/
│   ├── my_date_schema.py    # Pydantic schema for guardrail validation
│
│── my_config/
│   ├── gemini_config.py     # Gemini API client + model configuration
│
│── main.py                  # Entry point (run queries)
│── README.md                # Project documentation
```

## 🏨 Hotel Data Example
Defined in hotel_assistant.py
```python
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
```

## 🚀 Usage
Run the project with:
```bash
python main.py
```

Example output:
```sql
There are 140 rooms available at Hotel Green Valley. 
We have a total of 150 rooms, but 10 are reserved for special guests.
```

## 🔑 Key Features
✅ Dynamic agent creation for multiple hotels
✅ Guardrails for query validation
✅ Gemini integration with OpenAI Agents SDK
✅ Clear modular structure
