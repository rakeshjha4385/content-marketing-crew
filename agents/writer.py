from crewai import Agent
from tools.notion import notion_search_tool

class WriterAgent:
    def __init__(self):
        self.agent = Agent(
            role='Content Writer',
            goal='Create engaging, well-structured content based on research',
            backstory="""You're an experienced content writer with expertise in 
            transforming complex information into compelling narratives. You have 
            worked with major publications and know how to craft content that 
            resonates with target audiences.""",
            verbose=True,
            tools=[notion_search_tool],
            memory=True
        )