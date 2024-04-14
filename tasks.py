from crewai import Task
from agent import MyAgentFactory

class MyTaskFactory:
    def __init__(self):
        self.agent_factory = MyAgentFactory()

    def create_research_task(self):
        researcher = self.agent_factory.create_senior_researcher_agent()
        return Task(
            description=(
                "Identify the next big trend in {topic}. "
                "Focus on identifying pros and cons and the overall narrative. "
                "Your final report should clearly articulate the key points, "
                "its market opportunities, and potential risks."
            ),
            expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',
            tools=[researcher.tools[0]],
            agent=researcher,
        )

    def create_write_task(self):
        writer = self.agent_factory.create_writer_agent()
        return Task(
            description=(
                "Compose an insightful article on {topic}. "
                "Focus on the latest trends and how it's impacting the industry. "
                "This article should be easy to understand, engaging, and positive."
            ),
            expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
            tools=[writer.tools[0]],
            agent=writer,
            async_execution=False,
            output_file='new-blog-post.md'
        )
