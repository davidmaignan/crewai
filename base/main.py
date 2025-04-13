import os
from crewai import Agent, Task, Crew
from dotenv import load_dotenv
load_dotenv()


info_agent = Agent(
    role="Information Agent",
    goal="Give compelling information about certain topics",
    backstory="""
     You love to know information. People love and hate you for it. You win most of the
     quizzes at your local pub.
    """,
)

info_task = Task(
    description="Tell me all about the blue-ringed octopus",
    expected_output="Give me a quick summary and then also give me 7 bullets points describing it",
    agent=info_agent,
)

crew = Crew(
    agents=[info_agent],
    tasks=[info_task],
    verbose=True,
)

result = crew.kickoff()

print("-" * 100)
print(result)
