from crewai import Task
from textwrap import dedent

class ResearchTasks:
    def __init__(self, topic: str):
        self.topic = topic

    def gather_trends(self, agent):
        """Task to find trending subtopics using search tools"""
        return Task(
            description=dedent(f"""
                Research the latest trends and popular subtopics related to '{self.topic}'.
                Focus on identifying:
                - Emerging keywords (e.g., "AI content personalization")
                - High-engagement content formats (e.g., listicles, case studies)
                - Authoritative sources in this niche
            """),
            agent=agent,
            expected_output=dedent("""
                A markdown report with:
                - 5-7 trending subtopics
                - Data sources (URLs)
                - Key statistics (e.g., "70% marketers use AI for SEO")
            """)
        )

    def analyze_competitors(self, agent):
        """Task to study competitor content strategies"""
        return Task(
            description=dedent(f"""
                Analyze top 3 competitors publishing about '{self.topic}'.
                Identify their:
                - Content gaps
                - Most shared articles
                - Tone/style (professional vs. casual)
            """),
            agent=agent,
            expected_output="Competitor analysis table with strengths/weaknesses",
            context=[self.gather_trends(agent)]  # Requires prior trend data
        )