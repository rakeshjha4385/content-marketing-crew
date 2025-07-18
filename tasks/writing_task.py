from crewai import Task
from textwrap import dedent

class WritingTasks:
    def __init__(self, topic: str, research_data: str):
        self.topic = topic
        self.research_data = research_data

    def draft_blog_post(self, agent):
        """Task to generate SEO-optimized content"""
        return Task(
            description=dedent(f"""
                Write a 1000-word blog post about '{self.topic}' using this research:
                {self.research_data}
                
                Follow these rules:
                1. Use H2/H3 headings
                2. Include 3+ external links
                3. Apply 'Skyscraper Technique' to improve existing content
            """),
            agent=agent,
            expected_output="Full blog post in markdown format",
            output_file="output/blog_draft.md"  # Saves automatically
        )

    def proofread_content(self, agent):
        """Quality assurance task"""
        return Task(
            description=dedent("""
                Review the drafted blog post for:
                - Grammar/spelling errors
                - Readability (Hemingway score >70)
                - SEO best practices (keyword density 1-2%)
            """),
            agent=agent,
            expected_output="Revised version with tracked changes",
            context=[self.draft_blog_post(agent)]  # Depends on draft
        )