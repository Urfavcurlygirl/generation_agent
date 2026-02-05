import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_core.tools import tool
# initialize_agent is removed in modern LangChain, we use create_react_agent from langgraph
from langgraph.prebuilt import create_react_agent

load_dotenv()

# --- La partie Générateur de noms (Simple) ---
def generate_pet_name(animal_type, pet_color):
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
    
    prompt = PromptTemplate(
        input_variables=["pet_type", "pet_color"],
        template="I have a {pet_type} pet and I want a cool name for it. It is {pet_color} in color. Suggest me five cool names."
    )
    
    chain = prompt | llm
    response = chain.invoke({"pet_type": animal_type, "pet_color": pet_color})
    return response.content

# --- La partie Agent (Comme dans la vidéo) ---
# --- La partie Agent (Comme dans la vidéo) ---
def langchain_agent():
    # Temperature à 0 pour plus de déterministe et éviter les erreurs de format d'outils
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.0)

    # On définit un outil de calcul plus robuste pour les modèles Chat
    @tool
    def calculator(expression: str) -> str:
        """Calculate the result of a mathematical expression. 
        Input should be a string containing a mathematical expression (e.g., "12 * 2").
        Do not include "calculator" in the input string, just the expression."""
        try:
            # Sécurité basique
            allowed_chars = "0123456789+-*/(). "
            if not all(c in allowed_chars for c in expression):
                return "Invalid characters in expression"
            return str(eval(expression, {"__builtins__": None}, {}))
        except Exception as e:
            return f"Error: {e}"

    # On charge les outils. Note: "llm-math" est remplacé par notre calculator compatible Chat.
    tools = load_tools(["wikipedia"], llm=llm)
    tools.append(calculator)

    # On initialise l'agent (Updated for modern LangChain / LangGraph)
    agent_executor = create_react_agent(llm, tools)

    # On lance l'agent
    question = "What is the average life expectancy of a dog? Multiply that number by 2."
    
    print(f"Question: {question}")
    print("-" * 50)
    
    # Pour avoir le mode "verbose", on utilise stream et on affiche les messages au fur et à mesure
    # Cela permet de voir le "thinking process"
    last_message_count = 0
    final_response = ""
    
    # On utilise stream_mode="values" pour récupérer l'état des messages à chaque étape
    for step in agent_executor.stream({"messages": [("user", question)]}, stream_mode="values"):
        messages = step["messages"]
        
        # On affiche seulement les nouveaux messages
        if len(messages) > last_message_count:
            new_msgs = messages[last_message_count:]
            for msg in new_msgs:
                msg.pretty_print()
                print("-" * 50) # Séparateur visuel
                
            last_message_count = len(messages)
            
        # On garde la réponse finale (contenu du dernier message de l'assistant)
        if messages:
            final_response = messages[-1].content

    return final_response

if __name__ == "__main__":
    # Le print final est redondant car pretty_print affiche déjà tout, 
    # mais on le garde pour respecter la structure demandée
    result = langchain_agent()
    print("\n--- Final Result ---")
    print(result)
