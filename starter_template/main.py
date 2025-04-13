import os
from crewai import Crew
# from decouple import config
from agents import CustomAgents
from tasks import CustomTasks

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") or ""


class CustomCrew:
    def __init__(self, var1):
        self.var1 = var1

    def run(self):
        agents = CustomAgents()
        tasks = CustomTasks()

        pdf_agent = agents.pdf_agent()
        writer_agent = agents.writer_agent()

        pdf_task = tasks.pdf_task(pdf_agent, self.var1)
        writer_task = tasks.writer_task(writer_agent)

        crew = Crew(
            agents=[pdf_agent, writer_agent],
            tasks=[pdf_task, writer_task],
            verbose=True,
        )

        return crew.kickoff()


if __name__ == "__main__":
    print("##Welcome to the PDF RAG Crew##")
    print("--------------------------------")
    var1 = input("Enter the text you want to search for: ")

    crew = CustomCrew(var1)
    result = crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print(result)
    print("########################")
