from crewai import Tool
from slack_sdk import WebClient
import os
from dotenv import load_dotenv

load_dotenv()

class SlackTools:
    def __init__(self):
        self.client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))

    def send_message(self, message: str):
        """Send message to predefined Slack channel"""
        try:
            response = self.client.chat_postMessage(
                channel=os.getenv("SLACK_CHANNEL_ID"),
                text=message
            )
            return f"Message sent to Slack: {response['ts']}"
        except Exception as e:
            return f"Error sending Slack message: {str(e)}"

    def send_thread_reply(self, thread_ts: str, message: str):
        """Reply to an existing Slack thread"""
        try:
            response = self.client.chat_postMessage(
                channel=os.getenv("SLACK_CHANNEL_ID"),
                thread_ts=thread_ts,
                text=message
            )
            return f"Thread reply sent: {response['ts']}"
        except Exception as e:
            return f"Error replying to Slack thread: {str(e)}"

# CrewAI Tools
slack_notification_tool = Tool(
    name="Slack Notification",
    func=SlackTools().send_message,
    description="Sends notifications to the designated Slack channel"
)

slack_thread_tool = Tool(
    name="Slack Thread Reply",
    func=SlackTools().send_thread_reply,
    description="Replies to an existing Slack thread"
)