import os

from composio_crewai import Action, App, ComposioToolset
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if OPENAI_API_KEY is None:
    print("Please set OPENAI_API_KEY environment variable in the .env file")
    exit(1)

llm = ChatOpenAI(model="gpt-4-turbo", openai_api_key=OPENAI_API_KEY)

notion_composio_toolset = ComposioToolset(apps=[App.NOTION])
slack_composio_toolset = ComposioToolset(apps=[App.SLACK])


@CrewBase
class ClientCrew:
    """Class representing the Client crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def researcher(self) -> Agent:
        """Create a researcher agent"""
        return Agent(
            config=self.agents_config["researcher"],
            verbose=True,
            llm=llm,
        )

    @agent
    def reporting_analyst(self) -> Agent:
        """Create a reporting analyst agent"""
        return Agent(
            config=self.agents_config["reporting_analyst"], verbose=True, llm=llm
        )

    @agent
    def notion_agent(self) -> Agent:
        """Create a notion agent"""
        return Agent(
            config=self.agents_config["notion_agent"],
            verbose=True,
            tools=notion_composio_toolset,
            llm=llm,
        )

    @agent
    def slack_agent(self) -> Agent:
        """Create a slack agent"""
        return Agent(
            config=self.agents_config["slack_agent"],
            verbose=True,
            tools=slack_composio_toolset,
            llm=llm,
        )

    @task
    def research_task(self) -> Task:
        """Create a research task"""
        return Task(config=self.tasks_config["research_task"], agent=self.researcher())

    @task
    def reporting_task(self) -> Task:
        """Create a reporting task"""
        return Task(
            config=self.tasks_config["reporting_task"],
            agent=self.reporting_analyst(),
            output_file="report.md",
        )

    @task
    def notion_task(self) -> Task:
        """Create a notion task"""
        return Task(
            config=self.tasks_config["notion_task"],
            agent=self.notion_agent(),
            tools=notion_composio_toolset,
        )

    @task
    def slack_task(self) -> Task:
        """Create a slack task"""
        return Task(
            config=self.tasks_config["slack_task"],
            agent=self.slack_agent(),
            tools=slack_composio_toolset,
        )

    @crew
    def crew(self) -> Crew:
        """Create the Client crew"""
        return Crew(
            agents=self.agents, tasks=self.tasks, process=Process.sequential, verbose=2
        )
