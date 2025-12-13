from crewai import Agent
from src.tools.newsapi_tool import fetch_news
from src.tools.factcheck_tool import fact_check

def build_agents():
    news_agent = Agent(
        role="News Aggregator Agent",
        goal="Collect recent news articles on a given topic",
        tools=[fetch_news],
        verbose=True
    )

    summarization_agent = Agent(
        role="Summarization Agent",
        goal="Summarize articles and extract key factual claims",
        verbose=True
    )

    fact_checking_agent = Agent(
        role="Fact-Checking Agent",
        goal="Verify extracted claims using reliable fact-checking sources",
        tools=[fact_check],
        verbose=True
    )

    return news_agent, summarization_agent, fact_checking_agent
