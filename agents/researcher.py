from crewai import Agent
from tools.web_research import web_search_tool
from tools.notion import notion_search_tool

class ResearchAgent:
    def __init__(self):
        self.agent = Agent(
            role='Senior Research Analyst',
            goal='Provide comprehensive, accurate research on given topics',
            backstory="""You're an expert researcher with a decade of experience in 
            gathering and synthesizing information from diverse sources. You have a 
            knack for finding the most relevant data quickly.""",
            verbose=True,
            tools=[web_search_tool, notion_search_tool],
            memory=True
        )