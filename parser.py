import os
import json
from langchain_groq import ChatGroq
from dotenv import load_dotenv


from models import CVData

load_dotenv()


llm = ChatGroq(model="llama-3.3-70b-versatile")

structured_llm = llm.with_structured_output(CVData)

def parse_cv(text: str):
    prompt = f"""
You are an expert CV parser.

Extract all available information from the CV.
If a field is missing, leave it empty or null where appropriate.

CV:
{text}
"""

    try:
      return structured_llm.invoke(prompt)
    except Exception as e:
        raise ValueError(f"Falied to parse CV: {e}")



