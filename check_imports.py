try:
    from langgraph.prebuilt import create_react_agent
    print("langgraph.prebuilt.create_react_agent: FOUND")
except ImportError:
    print("langgraph.prebuilt.create_react_agent: NOT FOUND")

try:
    from langchain_community.agents import initialize_agent
    print("langchain_community.agents.initialize_agent: FOUND")
except ImportError:
    print("langchain_community.agents.initialize_agent: NOT FOUND")
