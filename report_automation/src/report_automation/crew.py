from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from .tools.web_search import WebSearchTool, ExtractTextTool

@CrewBase
class ReportAutomation:
    """Automated report generation crew"""
    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def topic_analyzer(self) -> Agent:
        return Agent(config=self.agents_config['topic_analyzer'], verbose=True)

    @agent
    def web_searcher(self) -> Agent:
        return Agent(config=self.agents_config['web_searcher'], verbose=True)

    @agent
    def content_extractor(self) -> Agent:
        return Agent(config=self.agents_config['content_extractor'], verbose=True)

    @agent
    def summarizer(self) -> Agent:
        return Agent(config=self.agents_config['summarizer'], verbose=True)

    @agent
    def report_generator(self) -> Agent:
        return Agent(config=self.agents_config['report_generator'], verbose=True)

    @task
    def keyword_task(self) -> Task:
        return Task(config=self.tasks_config['keyword_task'])

    @task
    def search_task(self) -> Task:
        return Task(config=self.tasks_config['search_task'], tools=[WebSearchTool()])

    @task
    def extract_task(self) -> Task:
        return Task(config=self.tasks_config['extract_task'], tools=[ExtractTextTool()])

    @task
    def summarize_task(self) -> Task:
        return Task(config=self.tasks_config['summarize_task'])

    @task
    def report_task(self) -> Task:
        return Task(config=self.tasks_config['report_task'], output_file='report.md')

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
