from config import OPENAI_API_KEY

if OPENAI_API_KEY is None:
    raise RuntimeError("OPENAI_API_KEY is not set")

print("API key is configured")