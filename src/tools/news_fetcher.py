from crewai_tools import BaseTool


class FetchNewsTool(BaseTool):
    """
    Tool for fetching news articles for a given topic.

    Attributes:
        name (str): Unique name of the tool.
        description (str): Short description of what the tool does.
    """
    name = "fetch_news"
    description = "Fetches news articles from NewsAPI"

    def _run(self, topic: str):
        """
        Fetches news articles related to the given topic

        Parameters:
            topic (str): The topic or keyword to search articles for.

        Returns:
            List[Dict]: A list of articles, each article represented as a dictionary with keys "title", "content".
        """
        # TODO: plug in the API
        raise NotImplementedError()
