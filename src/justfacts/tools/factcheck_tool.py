import os
import requests
from crewai.tools import BaseTool


class FactCheckTool(BaseTool):
    name: str = "fact_check"
    description: str = "Verifies claims made in news articles using Google Fact-check API"

    def _run(self, claims: list[str]) -> dict:
        FACTCHECK_API_KEY = os.getenv("FACTCHECK_API_KEY")
        if not FACTCHECK_API_KEY:
            raise RuntimeError("Missing FACTCHECK_API_KEY environment variable.")

        results = []
        for claim in claims:
            data = self._query_api(claim, FACTCHECK_API_KEY)
            results.append(self._parse_response(claim, data))

        return results

    def _query_api(self, claim: str, api_key: str) -> dict:
        url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"
        params = {
            "query": claim,
            "key": api_key
        }

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        return response.json()

    def _parse_response(self, claim_text: str, data: dict) -> dict:
        claims_data = data.get("claims", [])
        if not claims_data:
            return {
                "claim": claim_text,
                "reviews": []
            }

        # Take the best-fitting claim
        best_claim = claims_data[0]
        reviews = []
        
        # Parse reviews limited to 3 reviews
        for review in best_claim.get("claimReview", [])[:3]:
            reviews.append({
                "text": review.get("textualRating", "unverified"),
                "source": review.get("publisher", {}).get("name", "unknown"),
                "url": review.get("url", "")
            })
        
        return {
            "claim": claim_text,
            "reviews": reviews
        }

