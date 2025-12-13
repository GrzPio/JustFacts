import os
import requests
from crewai import tool

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

@tool("fetch_news")
def fetch_news(topic: str) -> str:
    """Fetches recent news articles on a given topic via NewsAPI."""
    if not NEWS_API_KEY:
        return "Missing NEWS_API_KEY environment variable."

    url = "https://newsapi.org/v2/everything"
    params = {
        "q": topic,
        "language": "en",
        "pageSize": 3,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    articles = response.json().get("articles", [])

    if not articles:
        return "No articles found."

    text = ""
    for article in articles:
        title = article.get("title", "")
        description = article.get("description", "")
        text += f"TITLE: {title}\nDESCRIPTION: {description}\n\n"

    return text
