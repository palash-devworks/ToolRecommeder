from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI

from crewai_tools import SerperDevTool, ScrapeWebsiteTool


@CrewBase
class MarketResearchCrew():
    """Market Research Crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def market_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['market_researcher'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True
        )

    @agent
    def comparative_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['comparative_analyst'],
            verbose=True
        )

    @agent
    def requirements_clarifier(self) -> Agent:
        return Agent(
            config=self.agents_config['requirements_clarifier'],
			tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True
        )

    @agent
    def recommendation_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['recommendation_specialist'],
            verbose=True
        )

    @agent
    def industry_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['industry_expert'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True
        )

    @agent
    def technical_evaluator(self) -> Agent:
        return Agent(
            config=self.agents_config['technical_evaluator'],
            verbose=True
        )

    @agent
    def user_experience_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['user_experience_specialist'],
            verbose=True
        )

    @agent
    def cost_benefit_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['cost_benefit_analyst'],
            verbose=True
        )

    @agent
    def implementation_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['implementation_strategist'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            agent=self.market_researcher()
        )

    @task
    def comparison_task(self) -> Task:
        return Task(
            config=self.tasks_config['comparison_task'],
            agent=self.comparative_analyst()
        )

    @task
    def requirements_clarification_task(self) -> Task:
        return Task(
            config=self.tasks_config['requirements_clarification_task'],
            agent=self.requirements_clarifier()
        )

    @task
    def recommendation_task(self) -> Task:
        return Task(
            config=self.tasks_config['recommendation_task'],
            agent=self.recommendation_specialist(),
            output_file='report.md'
        )
    @task
    def industry_expert_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['industry_expert_analysis_task'],
            agent=self.industry_expert()
        )

    @task
    def technical_evaluation_task(self) -> Task:
        return Task(
            config=self.tasks_config['technical_evaluation_task'],
            agent=self.technical_evaluator()
        )

    @task
    def user_experience_assessment_task(self) -> Task:
        return Task(
            config=self.tasks_config['user_experience_assessment_task'],
            agent=self.user_experience_specialist()
        )

    @task
    def cost_benefit_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['cost_benefit_analysis_task'],
            agent=self.cost_benefit_analyst()
        )

    @task
    def implementation_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['implementation_strategy_task'],
            agent=self.implementation_strategist()
        )
    # @crew
    # def crew(self) -> Crew:
    #     """Creates the Market Research Crew"""
    #     return Crew(
    #         agents=self.agents,
    #         tasks=self.tasks,
    #         process=Process.sequential,
    #         verbose=False
    #     )

    @crew
    def crew(self) -> Crew:
        """Creates the Market Research Crew"""
        return Crew(
            agents=[
                self.market_researcher(),
                self.comparative_analyst(),
                self.requirements_clarifier(),
                self.recommendation_specialist(),
                self.industry_expert(),
                self.technical_evaluator(),
                self.user_experience_specialist(),
                self.cost_benefit_analyst(),
                self.implementation_strategist()
            ],
            tasks=[
                self.research_task(),
                self.comparison_task(),
                self.requirements_clarification_task(),
                self.industry_expert_analysis_task(),
                self.technical_evaluation_task(),
                self.user_experience_assessment_task(),
                self.cost_benefit_analysis_task(),
                self.implementation_strategy_task(),
                self.recommendation_task()
            ],
            process=Process.sequential,
            verbose=True
    )    