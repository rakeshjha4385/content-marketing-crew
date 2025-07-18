from crewai import Agent
from tools.notion_api import NotionClient
from tools.slack_notify import SlackClient
from typing import Optional

class ContentPublisher:
    def __init__(self, llm):
        self.notion = NotionClient()
        self.slack = SlackClient()
        
        self.agent = Agent(
            role="Content Publisher",
            goal="Distribute approved content to appropriate channels",
            backstory=(
                "A technical marketing specialist skilled in automating "
                "content distribution across digital platforms."
            ),
            tools=[
                self.publish_to_notion,
                self.notify_via_slack,
                self.log_publication
            ],
            verbose=True,
            llm=llm,
            memory=True
        )

    @tool
    def publish_to_notion(self, content: dict, database_id: str) -> bool:
        """Publish content to specified Notion database"""
        return self.notion.create_page(
            database_id=database_id,
            title=content['title'],
            content=content['body'],
            metadata={
                "status": "Published",
                "word_count": content['word_count']
            }
        )

    @tool
    def notify_via_slack(self, message: str, channel: str) -> bool:
        """Send notification to Slack channel"""
        return self.slack.post_message(
            channel=channel,
            text=f"New content published: {message}"
        )

    @tool
    def log_publication(self, content: dict) -> Optional[str]:
        """Record publication in audit log"""
        with open("publication_log.md", "a") as f:
            f.write(f"## {content['title']}\n\nPublished at {datetime.now()}\n\n")
        return "Publication logged"
