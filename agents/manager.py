from crewai import Agent
from tools.slack import slack_notification_tool
from tools.n8n_integration import n8n_trigger_tool

class ManagerAgent:
    def __init__(self):
        self.agent = Agent(
            role='Content Workflow Manager',
            goal='Oversee the entire content creation process and ensure quality and deadlines are met',
            backstory="""You're a seasoned content operations manager with experience coordinating
            complex publishing workflows. You excel at resource allocation, timeline management,
            and quality control across multiple concurrent projects.""",
            verbose=True,
            tools=[slack_notification_tool, n8n_trigger_tool],
            memory=True,
            allow_delegation=True
        )