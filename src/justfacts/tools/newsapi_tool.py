import os
import requests
from crewai.tools import BaseTool


class NewsAPITool(BaseTool):
    name = "fetch_news"
    description = "Fetches recent news articles for a given topic using NewsAPI"

    def _run(self, topic: str) -> list[dict]:
        NEWS_API_KEY = os.getenv("NEWS_API_KEY")
        if not NEWS_API_KEY:
            raise RuntimeError("Missing NEWS_API_KEY environment variable.")

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

        results = []
        for idx, article in enumerate(articles):
            results.append({
                "id": f"newsapi-{idx}",
                "title": article.get("title"),
                "content": article.get("content") or article.get("description")
                "source": article.get("source", {}).get("name"),
                "url": article.get("url"),
                "publication_date": article.get("publishedAt"),
            })

        return results
