from typing_extensions import TypedDict, NotRequired


class ChatState(TypedDict):
    user_query: str
    rag_response: NotRequired[str]
    sql_response: NotRequired[str]
    final_response: NotRequired[str]


def create_chat_state(query: str) -> ChatState:
    return ChatState(user_query=query)
