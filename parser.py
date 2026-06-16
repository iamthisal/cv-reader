import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-3.5-flash")

def parse_cv(text: str):

    prompt = f"""
    You are an expert in cv reading and extract the text data to structured json 
    Your task is to read the text file of cv and MaKE A JSON STRCTURE WITH:
    
    -name
    -email
    -skills(list)
    -experience(list , role, company, years)
    -education
    
    Rules
    -ONLY RETURN VALID JSON NOTHING ELSE
    -No explnations 
    -No markdown
    
    CV TEXT:
    {text}
     """

    response = model.generate_content(prompt)
    content = response.text

    return json.loads(content)