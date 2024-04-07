from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI
from composio_crewai import ComposioToolset, Action, App

# Uncomment the following line to use an example of a custom tool
# from serhant.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

OPENAI_API_KEY = ""  # Change the key with yours

llm = ChatOpenAI(model="gpt-4-turbo-preview", openai_api_key=OPENAI_API_KEY)

notionComposioToolset = ComposioToolset(apps=[App.NOTION])
slackComposioToolset = ComposioToolset(apps=[App.SLACK])


@CrewBase
class SerhantCrew:
    """Serhant crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            # tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
            verbose=True,
            llm=llm,
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["reporting_analyst"], verbose=True, llm=llm
        )

    @agent
    def notion_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["notion_agent"],
            verbose=True,
            tools=notionComposioToolset,
            llm=llm,
        )

    @agent
    def slack_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["slack_agent"],
            verbose=True,
            tools=slackComposioToolset,
            llm=llm,
        )

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config["research_task"], agent=self.researcher())

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config["reporting_task"],
            agent=self.reporting_analyst(),
            output_file="report.md",
        )

    @task
    def notion_task(self) -> Task:
        return Task(
            config=self.tasks_config["notion_task"],
            agent=self.notion_agent(),
            tools=notionComposioToolset,
        )

    @task
    def slack_task(self) -> Task:
        return Task(
            config=self.tasks_config["slack_task"],
            agent=self.slack_agent(),
            tools=slackComposioToolset,
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Serhant crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=2,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
