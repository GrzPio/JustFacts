from crewai_tools import BaseTool


class SummarizerTool(BaseTool):
    """
    Tool for summarizing a list of news articles into concise key points.
    """

    name = "article_summarizer"

    def _run(self, articles: list):
        """
        Summarizes the given articles.

        Parameters:
            articles (List[Dict]): list of articles, each a dictionary with keys "title", "content"

        Returns:
            List[str]: summaries for each article
        """
        raise NotImplementedError()
