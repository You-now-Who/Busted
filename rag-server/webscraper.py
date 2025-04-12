import requests
from dotenv import load_dotenv
import os

load_dotenv()

def search_links_google(query):
    api_key = os.getenv("G_CLOUD_KEY")
    cx = os.getenv("SEARCH_ID")
    search_url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cx}"
    try:
        response = requests.get(search_url)
        response.raise_for_status()
        results = response.json()
        links_and_snippets = [
            {"link": item["link"], "snippet": item["snippet"]}
            for item in results.get("items", [])
        ]
        return links_and_snippets
    except Exception as e:
        print(f"Error during Google Custom Search: {e}")
        return []