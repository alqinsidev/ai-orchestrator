from langgraph.graph import StateGraph, START, END
from src.state.chat_state import ChatState
from src.tools.sql_agent import sql_agent

workflow = StateGraph(ChatState)
workflow.add_node("sql", sql_agent)


workflow.add_edge(START, "sql")
workflow.add_edge("sql", END)


graph = workflow.compile()
