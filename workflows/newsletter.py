from crewai import Task
from tools.notion import notion_update_tool
from tools.slack import slack_notification_tool
from tools.n8n_integration import n8n_trigger_tool

def create_newsletter_workflow(theme, agents, audience="subscribers"):
    """Creates a newsletter production workflow"""
    
    # Content Collection Task
    collection_task = Task(
        description=f"""Collect relevant content for the {theme} newsletter targeting {audience}.
        Source 5-7 high-quality pieces including:
        - Company blog posts
        - Industry news
        - Curated external content
        - Upcoming events
        Ensure proper attribution and links for all content.""",
        agent=agents['researcher'].agent,
        expected_output="""A content collection including:
        - 5-7 content pieces with summaries
        - Proper attribution and links
        - Relevance score for each piece
        - Content type categorization""",
        tools=[slack_notification_tool]
    )

    # Curation Task
    curation_task = Task(
        description=f"""Curate the collected content into a cohesive newsletter about {theme}.
        Organize content into logical sections.
        Write engaging section headers and transitions.
        Create a narrative flow that connects all pieces.
        Draft a compelling subject line and preview text.""",
        agent=agents['writer'].agent,
        expected_output="""A newsletter draft containing:
        - Well-organized content sections
        - Engaging headers and transitions
        - Complete narrative flow
        - Subject line and preview text options""",
        context=[collection_task]
    )

    # Design Approval Task
    design_task = Task(
        description="""Prepare the newsletter for design:
        - Specify visual elements needed
        - Provide design direction
        - Identify key points for emphasis
        - Flag any special formatting requirements""",
        agent=agents['editor'].agent,
        expected_output="""Design specifications including:
        - Visual element requirements
        - Style guidelines
        - Content hierarchy
        - Special formatting notes""",
        context=[curation_task]
    )

    # Distribution Task
    distribution_task = Task(
        description="""Execute the newsletter distribution:
        - Upload final content to email platform
        - Configure audience segments
        - Set up A/B testing if applicable
        - Schedule send time
        - Prepare analytics tracking""",
        agent=agents['publisher'].agent,
        expected_output="""Distribution confirmation including:
        - Audience selection confirmation
        - Send schedule
        - Tracking setup
        - Final approval""",
        tools=[n8n_trigger_tool, notion_update_tool],
        context=[design_task]
    )

    return distribution_task