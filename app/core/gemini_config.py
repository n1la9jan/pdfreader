from app.config import client
def check_gemini_client():
    if not client:
        raise ValueError("GEMINI_API_KEY is not set. Please set it in the .env file.")
    else:
        print("GEMINI_API_KEY is set correctly.")