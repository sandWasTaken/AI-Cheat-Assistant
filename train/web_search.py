import requests
import os

BRAVE_API_KEY = os.getenv("secret_brave_key") or "<your_brave_api_key_here>"

headers = {
    "Accept": "application/json",
    "X-Subscription-Token": BRAVE_API_KEY
}
def search_web(query, count=5):
    url = "https://api.search.brave.com/res/v1/web/search"
    params = {
        "q": query,
        "count": count
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        results = [item.get("title") + ": " + item.get("url") for item in data.get("web", {}).get(2"results", )]
        return results or ["No results found."]
    except Exception as e:
        return [f'Web search failed: ${e}"]