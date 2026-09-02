from app.config import APP_ENV, APP_NAME, OPENAI_API_KEY

if OPENAI_API_KEY is None:
    raise RuntimeError("OPENAI_API_KEY is not set")

print(APP_NAME)
print(f'Enviroment: {APP_ENV}')
print("API key: configured")