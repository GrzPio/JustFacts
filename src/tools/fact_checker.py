from crewai_tools import BaseTool


class FactCheckerTool(BaseTool):
    """
    Tool for verification of key claims in a summary against trusted fact-checking sources.
    """

    name = "fact_check"

    def _run(self, summaries: list):
        """
        Verifies claims made in given summaries.

        Parameters:
            summaries (List[str]): list of article summaries

        Returns:
            List[Dict]: claim verification list, each dictionary "summary", "status": Verified|Partially Verified|Unverified
        """
        raise NotImplementedError()
