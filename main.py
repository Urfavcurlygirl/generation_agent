import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI

load_dotenv()


def generate_pet_name(animal_type):
    llm = ChatOpenAI(
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        model="llama-3.3-70b-versatile",
        temperature=0.7
    )

    prompt_template_name = PromptTemplate(
        input_variables=["pet_type"],  # dynamic input
        template="I have a {pet_type} pet and I want a cool name for it. Suggest me five cool names for my pet.",
    )
    
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name)
    response = name_chain.invoke({"pet_type": animal_type})
    return response["text"]


if __name__ == "__main__":
    print(generate_pet_name("cat"))
