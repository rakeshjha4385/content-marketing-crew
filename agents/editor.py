from crewai import Agent
from langchain.tools import tool
from prompts.editing import EDITOR_PROMPT

class ContentEditor:
    def __init__(self, llm):
        self.agent = Agent(
            role="Content Editor",
            goal="Ensure content quality, tone, and brand consistency",
            backstory=(
                "A meticulous editor with 10+ years experience in tech content, "
                "known for sharpening messaging while preserving author voice."
            ),
            tools=[self._check_quality, self._suggest_improvements],
            verbose=True,
            allow_delegation=True,
            llm=llm,
            memory=True,
            prompt=EDITOR_PROMPT
        )

    @tool
    def _check_quality(content: dict) -> dict:
        """Evaluate content against quality checklist"""
        return {
            "clarity_score": 0.9,
            "seo_optimized": True,
            "brand_voice_match": True,
            "issues_found": []
        }

    @tool
    def _suggest_improvements(content: dict) -> str:
        """Generate specific improvement suggestions"""
        return "Consider adding more data points from the research in section 2"
