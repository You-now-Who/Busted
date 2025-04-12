from google import genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_KEY"))

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Who are you and what is your use?"
)
print(response.text)
