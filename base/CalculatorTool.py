from crewai.tools import tool


@tool("Name of my tool")
def calculate(equation: str) -> str:
    """Clear description for what this tool is useful for, your agent will need this information to use it."""
    # Function logic here
    return equation
