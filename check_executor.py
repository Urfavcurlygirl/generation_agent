try:
    from langchain.agents import AgentExecutor, create_react_agent
    print("AgentExecutor and create_react_agent found in langchain.agents")
except ImportError as e:
    print(f"Error in langchain.agents: {e}")

try:
    from langchain.agents import initialize_agent
    print("initialize_agent found")
except ImportError:
    print("initialize_agent NOT found")
