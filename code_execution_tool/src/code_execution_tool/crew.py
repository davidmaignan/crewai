from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import CodeInterpreterTool, FileWriterTool


@CrewBase
class CodeExecutionTool():
    """CodeExecutionTool crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'


    @agent
    def execution_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['execution_agent'], # type: ignore
            tools=[CodeInterpreterTool()],
            verbose=True
        )
    
    @agent
    def writer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['writer_agent'], # type: ignore
            tools=[FileWriterTool()],
            verbose=True
        )


    @task
    def execution_task(self) -> Task:
        return Task(
            config=self.tasks_config['execution_task'], # type: ignore
        )

    @task
    def write_task(self) -> Task:
        return Task(
            config=self.tasks_config['write_task'], # type: ignore
        )


    @crew
    def crew(self) -> Crew:
        """Creates the CodeExecutionTool crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator # type: ignore
            tasks=self.tasks, # Automatically created by the @task decorator # type: ignore
            process=Process.sequential,
            verbose=True,
        )
