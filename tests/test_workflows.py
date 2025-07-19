import pytest
from unittest.mock import Mock, patch
from workflows.blog_post import create_blog_post_workflow
from workflows.social_media import create_social_media_workflow
from workflows.newsletter import create_newsletter_workflow
from crewai import Task

class TestBlogPostWorkflow:
    def test_workflow_structure(self):
        mock_agents = {
            'researcher': Mock(),
            'writer': Mock(),
            'editor': Mock(),
            'publisher': Mock(),
            'manager': Mock()
        }
        
        workflow = create_blog_post_workflow("Test Topic", mock_agents)
        
        assert isinstance(workflow, Task)
        assert workflow.agent == mock_agents['manager'].agent
        assert len(workflow.context) == 4  # Should have 4 dependent tasks

    def test_task_dependencies(self):
        mock_agents = {
            'researcher': Mock(),
            'writer': Mock(),
            'editor': Mock(),
            'publisher': Mock(),
            'manager': Mock()
        }
        
        workflow = create_blog_post_workflow("Test Topic", mock_agents)
        
        # Check the task chain
        research_task = workflow.context[0]
        writing_task = workflow.context[1]
        editing_task = workflow.context[2]
        publishing_task = workflow.context[3]
        
        assert research_task.agent == mock_agents['researcher'].agent
        assert writing_task.context == [research_task]
        assert editing_task.context == [writing_task]
        assert publishing_task.context == [editing_task]

class TestSocialMediaWorkflow:
    def test_platform_specific_content(self):
        mock_agents = {
            'researcher': Mock(),
            'writer': Mock(),
            'editor': Mock(),
            'publisher': Mock()
        }
        
        workflow = create_social_media_workflow("Test Topic", mock_agents, ["twitter", "linkedin"])
        
        content_task = workflow.context[1]  # Content creation is second task
        assert "Twitter: 280 chars max" in content_task.description
        assert "LinkedIn: longer form" in content_task.description
        assert "3 variations for each platform" in content_task.expected_output

    def test_approval_workflow(self):
        mock_agents = {
            'researcher': Mock(),
            'writer': Mock(),
            'editor': Mock(),
            'publisher': Mock()
        }
        
        workflow = create_social_media_workflow("Test Topic", mock_agents)
        
        approval_task = workflow.context[2]  # Approval is third task
        assert "brand voice consistency" in approval_task.description
        assert "revision notes" in approval_task.expected_output
        assert approval_task.agent == mock_agents['editor'].agent

class TestNewsletterWorkflow:
    def test_audience_targeting(self):
        mock_agents = {
            'researcher': Mock(),
            'writer': Mock(),
            'editor': Mock(),
            'publisher': Mock()
        }
        
        workflow = create_newsletter_workflow("Test Theme", mock_agents, "premium_subscribers")
        
        collection_task = workflow.context[0]
        assert "premium_subscribers" in collection_task.description
        assert "5-7 high-quality pieces" in collection_task.expected_output

    def test_design_specifications(self):
        mock_agents = {
            'researcher': Mock(),
            'writer': Mock(),
            'editor': Mock(),
            'publisher': Mock()
        }
        
        workflow = create_newsletter_workflow("Test Theme", mock_agents)
        
        design_task = workflow.context[2]
        assert "visual elements needed" in design_task.description
        assert "Content hierarchy" in design_task.expected_output
        assert design_task.agent == mock_agents['editor'].agent

    def test_distribution_tools(self):
        mock_agents = {
            'researcher': Mock(),
            'writer': Mock(),
            'editor': Mock(),
            'publisher': Mock()
        }
        
        workflow = create_newsletter_workflow("Test Theme", mock_agents)
        
        dist_task = workflow  # Final task is distribution
        assert n8n_trigger_tool in [tool.name for tool in dist_task.tools]
        assert "Configure audience segments" in dist_task.description