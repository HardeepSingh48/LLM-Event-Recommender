from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

llm = OllamaLLM(model="mistral")

def extract_preferences(message):
    prompt = PromptTemplate.from_template(
        "Extract event preferences and city from: {input}"
    )
    return llm.invoke(prompt.format(input=message))
