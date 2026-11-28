from src.config import get_settings

settings = get_settings()

print("OLLAMA_API_KEY:", settings.ollama_api_key)
print("OpenAI Model:", settings.openai_model)