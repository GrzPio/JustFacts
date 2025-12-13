import os
import requests
from crewai import tool

FACTCHECK_API_KEY = os.getenv("FACTCHECK_API_KEY")

@tool("fact_check")
def fact_check(claim: str) -> str:
    """Checks claims using Google Fact Check Tools API."""
    if not FACTCHECK_API_KEY:
        return "Missing FACTCHECK_API_KEY environment variable."

    url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"
    params = {
        "query": claim,
        "key": FACTCHECK_API_KEY
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    claims = data.get("claims", [])
    if not claims:
        return "No fact-check results found."

    results = []
    for c in claims[:3]:
        text = c.get("text", "N/A")
        reviews = c.get("claimReview", [])
        if reviews:
            rating = reviews[0].get("textualRating", "N/A")
            source = reviews[0].get("publisher", {}).get("name", "N/A")
            results.append(f"- {text} → {rating} ({source})")

    return "\n".join(results)
