from crewai import Task
from tools.slack import slack_notification_tool

def create_blog_post_workflow(topic, agents):
    # Research Task
    research_task = Task(
        description=f"""Conduct thorough research on the topic: {topic}. 
        Gather at least 5 recent, credible sources. Identify key points, 
        statistics, and opposing viewpoints.""",
        agent=agents['researcher'].agent,
        expected_output="A comprehensive research report with sources, key points, and statistics."
    )

    # Writing Task
    writing_task = Task(
        description=f"""Write a 1500-word blog post on {topic} using the research provided. 
        The post should include an engaging introduction, clear sections with subheadings, 
        and a compelling conclusion. Use markdown formatting.""",
        agent=agents['writer'].agent,
        expected_output="A complete blog post in markdown format.",
        context=[research_task]
    )

    # Editing Task
    editing_task = Task(
        description="""Review and edit the blog post for clarity, coherence, grammar, 
        and SEO optimization. Ensure the tone is consistent and appropriate for our audience.""",
        agent=agents['editor'].agent,
        expected_output="A polished version of the blog post with tracked changes.",
        context=[writing_task]
    )

    # Publishing Task
    publishing_task = Task(
        description="""Prepare the final blog post for publication. Format it according 
        to our CMS requirements and schedule it for publishing.""",
        agent=agents['publisher'].agent,
        expected_output="Confirmation of successful publication with a URL.",
        tools=[slack_notification_tool],
        context=[editing_task]
    )

    # Management Task
    management_task = Task(
        description="""Oversee the entire blog post creation process. Ensure all tasks 
        are completed on time and to standard. Handle any issues that arise.""",
        agent=agents['manager'].agent,
        expected_output="A summary report of the entire workflow execution.",
        context=[research_task, writing_task, editing_task, publishing_task]
    )

    return management_task