from crewai_tools import BaseTool


class MyCustomTool(BaseTool):
    """
    A custom tool for performing specific tasks.
    """

    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )

    def _run(self, argument: str) -> str:
        """
        Execute the tool with the provided argument.

        Args:
            argument (str): The argument for the tool.

        Returns:
            str: The output of the tool.
        """
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."
