from crewai import Agent
from tools.web_search import search_web

researcher = Agent(
  role="Content Researcher",
  goal="Find trending topics in AI-driven marketing",
  backstory="Expert in scraping blogs, reports, and social media for insights.",
  tools=[search_web],
  verbose=True,
  memory=True  # Enables conversation history
)