from crewai import Agent
from langchain.tools import tool
from prompts.writing import WRITER_PROMPT

class ContentWriter:
    def __init__(self, llm):
        self.agent = Agent(
            role="Content Writer",
            goal="Create engaging, SEO-optimized content based on research",
            backstory=(
                "A seasoned content creator with expertise in transforming "
                "technical research into compelling narratives for marketing teams."
            ),
            tools=[self._format_output],
            verbose=True,
            allow_delegation=False,
            llm=llm,
            max_iter=5,
            memory=True,
            prompt=WRITER_PROMPT
        )

    @tool
    def _format_output(content: str) -> dict:
        """Structure content into marketing-ready format"""
        return {
            "title": content.split("\n")[0].replace("#", "").strip(),
            "body": "\n".join(content.split("\n")[1:]),
            "keywords": ["AI", "content marketing", "automation"],
            "word_count": len(content.split())
        }
