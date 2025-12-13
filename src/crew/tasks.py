from crewai import Task

def build_tasks(topic, news_agent, summarization_agent, fact_checking_agent):
    task_news = Task(
        description=f"Fetch recent news articles about: {topic}",
        agent=news_agent
    )

    task_summary = Task(
        description=(
            "Summarize the provided news articles. "
            "Then list 3–5 atomic factual claims under the heading 'CLAIMS:'."
        ),
        agent=summarization_agent
    )

    task_factcheck = Task(
        description=(
            "For each claim listed under 'CLAIMS:', verify it using the fact_check tool. "
            "Return a verdict for each claim."
        ),
        agent=fact_checking_agent
    )

    return [task_news, task_summary, task_factcheck]
