from langgraph.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model
from icecream import ic
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.runnables import RunnableConfig
from pydantic import BaseModel


class WeatherResponse(BaseModel):
    conditions: str


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


checkpointer = InMemorySaver()
model = init_chat_model(
    "ollama:llama3.2",
    temperature=0
)

agent = create_react_agent(
    model=model,
    tools=[get_weather],
    checkpointer=checkpointer,
    response_format=WeatherResponse
)

# Run the agent
config: RunnableConfig = {"configurable": {"thread_id": "1"}}
sf_response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
    config
)
ny_response = agent.invoke(
    {"messages": [{"role": "user", "content": "what about new york?"}]},
    config
)

ic(ny_response)
