from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from langchain_community.tools.pubmed.tool import PubmedQueryRun


@CrewBase
class Hack4SyriaMedai:
    """Hack4SyriaMedai crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def translation_agent(self) -> Agent:
        print(f"Translation agent config: {self.agents_config['translation_agent']}")
        return Agent(config=self.agents_config["translation_agent"], verbose=True)

    @agent
    def privacy_agent(self) -> Agent:
        return Agent(config=self.agents_config["privacy_agent"], verbose=True)

    @agent
    def first_line_support_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["first_line_support_agent"], verbose=True
        )

    @agent
    def diagnosis_agent(self) -> Agent:
        return Agent(config=self.agents_config["diagnosis_agent"], verbose=True)

    @agent
    def cardiology_specialist_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["cardiology_specialist_agent"], verbose=True
        )

    @agent
    def medical_knowledge_agent(self) -> Agent:
        return Agent(config=self.agents_config["medical_knowledge_agent"], verbose=True)

    @agent
    def final_output_agent(self) -> Agent:
        return Agent(config=self.agents_config["final_output_agent"], verbose=True)

    @task
    def translation_to_ar(self) -> Task:
        print(f"{self.tasks_config['translation_to_ar']}")
        return Task(
            config=self.tasks_config["translation_to_ar"],
            agent=self.translation_agent(),
        )

    @task
    def privacy_check(self) -> Task:
        return Task(
            config=self.tasks_config["privacy_check"],
            agent=self.privacy_agent(),
        )

    @task
    def information_gathering(self) -> Task:
        return Task(
            config=self.tasks_config["information_gathering"],
            agent=self.first_line_support_agent(),
        )

    @task
    def initial_diagnosis(self) -> Task:
        return Task(
            config=self.tasks_config["initial_diagnosis"],
            agent=self.diagnosis_agent(),
        )

    @task
    def cardiac_consultation(self) -> Task:
        return Task(
            config=self.tasks_config["cardiac_consultation"],
            agent=self.cardiology_specialist_agent(),
        )

    @task
    def medical_validation(self) -> Task:
        return Task(
            config=self.tasks_config["medical_validation"],
            agent=self.medical_knowledge_agent(),
            tools=[SerperDevTool()],
        )

    @task
    def final_report_generation(self) -> Task:
        return Task(
            config=self.tasks_config["final_report_generation"],
            agent=self.final_output_agent(),
        )

    @task
    def final_translation(self) -> Task:
        return Task(
            config=self.tasks_config["final_translation"],
            agent=self.translation_agent(),
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Hack4SyriaMedai crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
