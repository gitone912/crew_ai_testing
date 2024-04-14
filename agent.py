import os
from crewai import Agent
from crewai_tools import SerperDevTool

class MyAgentFactory:
    def __init__(self):
        os.environ["SERPER_API_KEY"] = "05bcb57291ba42d046326f1a595c0cadc3fbb9f7"  # serper.dev API key
        os.environ["OPENAI_API_KEY"] = "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"
        self.search_tool = SerperDevTool()

    def create_senior_researcher_agent(self):
        return Agent(
            role='Senior Researcher',
            goal='Uncover groundbreaking technologies in {topic}',
            verbose=True,
            memory=True,
            backstory=(
                "Driven by curiosity, you're at the forefront of "
                "innovation, eager to explore and share knowledge that could change "
                "the world."
            ),
            tools=[self.search_tool],
            allow_delegation=True
        )

    def create_writer_agent(self):
        return Agent(
            role='Writer',
            goal='Narrate compelling tech stories about {topic}',
            verbose=True,
            memory=True,
            backstory=(
                "With a flair for simplifying complex topics, you craft "
                "engaging narratives that captivate and educate, bringing new "
                "discoveries to light in an accessible manner."
            ),
            tools=[self.search_tool],
            allow_delegation=False
        )
