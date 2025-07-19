import os
from dotenv import load_dotenv
from agents.researcher import ResearchAgent
from agents.writer import WriterAgent
from agents.editor import EditorAgent
from agents.publisher import PublisherAgent
from agents.manager import ManagerAgent
from workflows.blog_post import create_blog_post_workflow

load_dotenv()

def main():
    # Initialize agents
    researcher = ResearchAgent()
    writer = WriterAgent()
    editor = EditorAgent()
    publisher = PublisherAgent()
    manager = ManagerAgent()

    # Execute blog post workflow
    blog_post_task = create_blog_post_workflow(
        topic="The Future of AI in Content Marketing",
        agents={
            'researcher': researcher,
            'writer': writer,
            'editor': editor,
            'publisher': publisher,
            'manager': manager
        }
    )

    # Execute the task
    blog_post_task.execute()

if __name__ == "__main__":
    main()