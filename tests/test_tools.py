import pytest
from unittest.mock import Mock, patch
from tools.notion import NotionTools, notion_search_tool
from tools.slack import SlackTools, slack_notification_tool
from tools.web_research import WebResearchTools, web_search_tool

class TestNotionTools:
    @patch('tools.notion.Client')
    def test_search_database_success(self, mock_client):
        # Setup mock
        mock_instance = mock_client.return_value
        mock_instance.databases.query.return_value = {
            "results": [{
                "id": "123",
                "url": "https://notion.so/page",
                "last_edited_time": "2023-01-01",
                "properties": {
                    "Name": {
                        "type": "title",
                        "title": [{"plain_text": "Test Page"}]
                    }
                }
            }]
        }

        # Test
        tools = NotionTools()
        results = tools.search_database("test")
        
        # Assert
        assert len(results) == 1
        assert results[0]["title"] == "Test Page"
        assert results[0]["url"] == "https://notion.so/page"

    @patch('tools.notion.Client')
    def test_search_database_error(self, mock_client):
        mock_instance = mock_client.return_value
        mock_instance.databases.query.side_effect = Exception("API Error")
        
        tools = NotionTools()
        result = tools.search_database("test")
        
        assert "Error searching Notion" in result

class TestSlackTools:
    @patch('tools.slack.WebClient')
    def test_send_message_success(self, mock_client):
        mock_instance = mock_client.return_value
        mock_instance.chat_postMessage.return_value = {"ts": "12345"}
        
        tools = SlackTools()
        result = tools.send_message("test message")
        
        assert "Message sent to Slack" in result

    @patch('tools.slack.WebClient')
    def test_send_message_error(self, mock_client):
        mock_instance = mock_client.return_value
        mock_instance.chat_postMessage.side_effect = Exception("API Error")
        
        tools = SlackTools()
        result = tools.send_message("test message")
        
        assert "Error sending Slack message" in result

class TestWebResearchTools:
    @patch('tools.web_research.ddg')
    def test_search_web_success(self, mock_ddg):
        mock_ddg.return_value = [
            {"title": "Test", "link": "https://test.com", "body": "Test snippet"}
        ]
        
        tools = WebResearchTools()
        results = tools.search_web("test query")
        
        assert len(results) == 1
        assert results[0]["title"] == "Test"

    @patch('tools.web_research.ddg')
    def test_search_web_error(self, mock_ddg):
        mock_ddg.side_effect = Exception("Search Error")
        
        tools = WebResearchTools()
        result = tools.search_web("test query")
        
        assert "Error searching web" in result

    @patch('tools.web_research.requests.get')
    def test_scrape_website_success(self, mock_get):
        mock_response = Mock()
        mock_response.text = "<html><body>Test content</body></html>"
        mock_get.return_value = mock_response
        
        tools = WebResearchTools()
        result = tools.scrape_website("https://test.com")
        
        assert result["domain"] == "test.com"
        assert "Test content" in result["content"]

class TestToolWrappers:
    def test_notion_tool_wrapper(self):
        result = notion_search_tool("test")
        assert isinstance(result, (list, str))  # Returns either results or error string

    def test_slack_tool_wrapper(self):
        with patch.object(SlackTools, 'send_message', return_value="success"):
            result = slack_notification_tool("test")
            assert result == "success"

    def test_web_search_tool_wrapper(self):
        with patch.object(WebResearchTools, 'search_web', return_value=[]):
            result = web_search_tool("test")
            assert isinstance(result, list)