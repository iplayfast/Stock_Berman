from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
# from langchain_groq import ChatGroq
#from langchain.llms import Ollama
from langchain_community.llms import Ollama
#ollama_llm = Ollama(model="mixtral", base_url="https://11434:/v1")
ollama_llm = Ollama(model="mistral", base_url="http://localhost:11434")

@CrewBase
class FinancialAnalystCrew():
	"""FinancialAnalystCrew crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	def __init__(self) -> None:
		# self.groq_llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")
		self.llm = ollama_llm

	@agent
	def company_researcher(self) -> Agent:
		return Agent(
			config = self.agents_config['company_researcher'],
			llm = self.llm
		)

	@agent
	def company_analyst(self) -> Agent:
		return Agent(
			config = self.agents_config['company_analyst'],
			llm = self.llm
		)

	@task
	def research_company_task(self) -> Task:
		return Task(
			config = self.tasks_config['research_company_task'],
			agent = self.company_researcher()
		)

	@task
	def analyze_company_task(self) -> Task:
		return Task(
			config = self.tasks_config['analyze_company_task'],
			agent = self.company_analyst()
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the FinancialAnalystCrew crew"""
		return Crew(
			agents =  self.agents,
			tasks = self.tasks,
			process = Process.sequential,
			verbose = 2
		)
