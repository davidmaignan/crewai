import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import PDFSearchTool
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_PATH = os.path.join(SCRIPTS_DIR, "pdf", "agentops.pdf")

pdf_search_tool = PDFSearchTool(
    pdf_path=PDF_PATH,
    description="A tool to search for information in a PDF file",
)

@CrewBase
class PdfRag():
    """PdfRag crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def pdf_rag_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['pdf_rag_agent'], # type: ignore
            tools=[pdf_search_tool],
            verbose=True
        )

    @agent
    def pdf_summary_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['pdf_summary_agent'], # type: ignore
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def pdf_rag_task(self) -> Task:
        return Task(
            config=self.tasks_config['pdf_rag_task'], # type: ignore
        )

    @task
    def pdf_summary_task(self) -> Task:
        return Task(
            config=self.tasks_config['pdf_summary_task'], # type: ignore
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the PdfRag crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator # type: ignore
            tasks=self.tasks, # Automatically created by the @task decorator # type: ignore
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
