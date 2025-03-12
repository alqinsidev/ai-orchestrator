import requests
from src.state.chat_state import ChatState
from config import SQL_AGENT_BASEURL


def sql_agent(state: ChatState):
    body = {"query": state["user_query"]}
    response = requests.post(
        f"{SQL_AGENT_BASEURL}sql-agent", json=body
    )
    response = response.json().get("text")
    state["sql_response"] = response
    return state
