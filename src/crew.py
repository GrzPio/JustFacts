from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from typing import List
from tools.factcheck_tool import FactCheckTool
from tools.newsapi_tool import NewsAPITool


@CrewBase
class Justfacts:
    """Justfacts crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def aggregator(self) -> Agent:
        return Agent(
            verbose=True,
            tools=[NewsAPITool()]
        )

    @agent
    def summarizer(self) -> Agent:
        return Agent(
            verbose=True
        )

    @agent
    def fact_checker(self) -> Agent:
        return Agent(
            verbose=True,
            tools=[FactCheckTool()]
        )

    @task
    def fetch_news(self) -> Task:
        return Task()

    @task
    def summarize_article(self) -> Task:
        return Task()

    @task
    def fact_check(self) -> Task:
        return Task()

    @crew
    def crew(self) -> Crew:
        """Creates the Justfacts crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
