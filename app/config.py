from dotenv import load_dotenv
from os import getenv
from google import genai


load_dotenv()
api = getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api)