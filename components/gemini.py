import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Cache model so Streamlit doesn't re-load it every request
from functools import lru_cache

@lru_cache()
def load_model():
    return genai.GenerativeModel("gemini-1.5-flash")

model = load_model()

def get_gemini_response(prompt: str):
    try:
        response = model.generate_content(
            prompt,
            generation_config={
                "max_output_tokens": 2000,
                "temperature": 0.6,
                "top_p": 0.9
            }
        )
        return response.text

    except Exception as e:
        return f"❌ Gemini Error: {str(e)}"
