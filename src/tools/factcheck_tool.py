import os
import requests
from crewai_tools import BaseTool


class FactCheckTool(BaseTool):
    name = "fact_check"
    description = "Verifies claims made in news articles using Google Fact-check API"

    def _run(self, claims: list[str]) -> dict:
        FACTCHECK_API_KEY = os.getenv("FACTCHECK_API_KEY")
        if not FACTCHECK_API_KEY:
            raise RuntimeError("Missing FACTCHECK_API_KEY environment variable.")

        results = []
        for claim in claims:
            data = self._query_api(claim, FACTCHECK_API_KEY)
            results.append(self._parse_response(claim, data)

        return results

    def _query_api(self, claim: str, api_key: str) -> dict:
        url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"
        params = {
            "query": claim,
            "key": FACTCHECK_API_KEY
        }

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        return response.json()

    def _parse_response(self, claim: str, data: dict) -> dict:
        claims_data = data.get("claims", [])
        if not claims_data:
            return {
                "claim": claim,
                "verdict": "unverified",
                "sources": []
            }

        review = claims_data[0].get("claimReview", [{}])[0]
        rating = review.get("textualRating", "Unverified")
        source = review.get("publisher", {}).get("name", "Unknown")

        return {
            "claim": claim,
            "verdict": self._map_rating(rating),
            "sources": [source]
        }


    def _map_rating(self, rating: str) -> str:
        rating_lower = rating.lower()
        if "true" in rating_lower:
            return "verified"
        if "mixed" in rating_lower or "partly" in rating_lower:
            return "partially_verified"
        return "unverified"
