from google import genai
from dotenv import load_dotenv
import os
import requests

from webscraper import search_links_google

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_KEY"))


def scrape_web_context(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text[:500]
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ""

def generate_rag_response(query):
    search_results = search_links_google(query)
    contexts = []
    for result in search_results:
        link = result["link"]
        snippet = result["snippet"]
        print(f"Using snippet from: {link}")
        contexts.append(snippet)
    combined_context = " ".join(contexts)
    augmented_query = f"Context: {combined_context}\n\nQuery: {query}"
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=augmented_query
        )
        return response.text
    except Exception as e:
        print(f"Error generating response with Gemini: {e}")
        return "Failed to generate a response."

query = "Are dogs allergic to chocolate?"
response = generate_rag_response(query)
# response = search_links_google(query=query)
print(response)
