import pytest
from agents.researcher import ResearchAgent
from agents.writer import WriterAgent

class TestAgents:
    def test_researcher_agent_creation(self):
        researcher = ResearchAgent()
        assert researcher.agent.role == 'Senior Research Analyst'
        assert len(researcher.agent.tools) == 2
        
    def test_writer_agent_creation(self):
        writer = WriterAgent()
        assert writer.agent.role == 'Content Writer'
        assert len(writer.agent.tools) == 1