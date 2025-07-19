from crewai import Task
from tools.slack import slack_notification_tool
from tools.n8n_integration import n8n_trigger_tool

def create_social_media_workflow(topic, agents, platforms=["twitter", "linkedin"]):
    """Creates a social media content workflow for multiple platforms"""
    
    # Research Task
    research_task = Task(
        description=f"""Research trending angles and hashtags for the topic: {topic}.
        Find 3-5 recent successful posts on {', '.join(platforms)} about similar topics.
        Identify key engagement drivers and optimal posting times.""",
        agent=agents['researcher'].agent,
        expected_output=f"""A research report containing:
        - Trending hashtags and angles
        - Analysis of successful similar posts
        - Recommended posting times for each platform
        - Platform-specific best practices""",
        tools=[slack_notification_tool]
    )

    # Content Creation Task
    content_task = Task(
        description=f"""Create engaging social media content about {topic} for {', '.join(platforms)}.
        Craft platform-specific versions (Twitter: 280 chars max, LinkedIn: longer form).
        Include relevant hashtags and emojis where appropriate.
        Create 3 variations for each platform.""",
        agent=agents['writer'].agent,
        expected_output=f"""A set of social media posts including:
        - 3 Twitter post variations
        - 3 LinkedIn post variations
        - Appropriate hashtags and mentions
        - Platform-optimized formatting""",
        context=[research_task]
    )

    # Approval Task
    approval_task = Task(
        description="""Review and approve the social media content.
        Ensure brand voice consistency, proper tone, and compliance with guidelines.
        Provide constructive feedback if revisions are needed.""",
        agent=agents['editor'].agent,
        expected_output="""Approved social media content with:
        - Approval status for each variation
        - Any revision notes
        - Final selected versions""",
        context=[content_task]
    )

    # Scheduling Task
    scheduling_task = Task(
        description=f"""Schedule the approved social media posts.
        Use optimal posting times from research.
        Set up tracking UTM parameters for each post.
        Confirm scheduling with all platforms.""",
        agent=agents['publisher'].agent,
        expected_output="""Scheduling confirmation including:
        - Posting schedule for each platform
        - Tracking UTM parameters
        - Confirmation receipts from each platform""",
        tools=[n8n_trigger_tool],
        context=[approval_task]
    )

    return scheduling_task