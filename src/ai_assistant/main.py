from ai_assistant.config import GROQ_API_KEY

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set. Please set it in the .env file.")
else: 
    print("GROQ_API_KEY is set correctly.")