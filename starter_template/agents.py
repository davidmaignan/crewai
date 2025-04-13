from textwrap import dedent
from crewai import Agent
from langchain_openai import ChatOpenAI
from crewai_tools import PDFSearchTool


class CustomAgents:
    def __init__(self):
        self.phi3_14b = ChatOpenAI(
            model="ollama/phi3:14b", base_url="http://localhost:11434"
        )
        self.phi3_8b = ChatOpenAI(
            model="ollama/phi3:3.8b", base_url="http://localhost:11434"
        )
        self.gemma3_1b = ChatOpenAI(
            model="ollama/gemma3:1b", base_url="http://localhost:11434"
        )
        self.mistral_latest = ChatOpenAI(
            model="ollama/mistral:latest", base_url="http://localhost:11434"
        )

    def pdf_agent(self):
        pdf_tool = PDFSearchTool(pdf_path="gpt-4o-2024-02-15.pdf")

        return Agent(
            role="Senior PDF Analyst",
            backstory=dedent(
                """You are a senior PDF analyst with a deep understanding of the content of the PDF."""
            ),
            goal=dedent(
                """Uncover the most important information in the PDF and provide a detailed summary of the content."""
            ),
            tools=[pdf_tool],
            verbose=True,
            llm=self.phi3_8b,
        )

    def writer_agent(self):
        return Agent(
            role="Writer",
            backstory=dedent(
                """You are a senior PDF analyst with a deep understanding of the content of the PDF."""
            ),
            goal=dedent(
                """Uncover the most important information in the PDF and provide a detailed summary of the content."""
            ),
            tools=[],
            verbose=True,
            llm=self.phi3_8b,
        )
