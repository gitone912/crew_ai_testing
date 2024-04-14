from crewai import Crew, Process
from tasks import MyTaskFactory  # Importing MyTaskFactory from tasks module

class MyCrewManager:
    def __init__(self):
        self.task_factory = MyTaskFactory()

    def start_tasks_execution(self):
        research_task = self.task_factory.create_research_task()
        write_task = self.task_factory.create_write_task()

        crew = Crew(
            agents=[research_task.agent, write_task.agent],
            tasks=[research_task, write_task],
            process=Process.sequential,
            memory=True,
            cache=True,
            max_rpm=100,
            share_crew=True
        )
        result = crew.kickoff(inputs={'topic': 'AI in Mobile industry'})
        print(result)

if __name__ == "__main__":
    manager = MyCrewManager()
    manager.start_tasks_execution()
