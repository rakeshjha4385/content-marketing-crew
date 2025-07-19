from crewai import Tool
from notion_client import Client
import os
from dotenv import load_dotenv

load_dotenv()

class NotionTools:
    def __init__(self):
        self.client = Client(auth=os.getenv("NOTION_API_KEY"))

    def search_database(self, query: str):
        """Search Notion database for relevant information"""
        try:
            database_id = os.getenv("NOTION_DATABASE_ID")
            results = self.client.databases.query(
                database_id=database_id,
                filter={
                    "property": "Name",
                    "title": {
                        "contains": query
                    }
                }
            )
            return [self._parse_page(page) for page in results.get("results", [])]
        except Exception as e:
            return f"Error searching Notion: {str(e)}"

    def update_page(self, page_id: str, content: str):
        """Update a Notion page with new content"""
        try:
            self.client.pages.update(
                page_id=page_id,
                properties={
                    "Content": {
                        "rich_text": [{
                            "text": {
                                "content": content
                            }
                        }]
                    }
                }
            )
            return "Successfully updated Notion page"
        except Exception as e:
            return f"Error updating Notion page: {str(e)}"

    def _parse_page(self, page):
        """Parse Notion page into a readable format"""
        return {
            "id": page["id"],
            "title": self._get_page_title(page),
            "url": page["url"],
            "last_edited": page["last_edited_time"]
        }

    def _get_page_title(self, page):
        """Extract title from Notion page"""
        title_property = page.get("properties", {}).get("Name", {})
        if title_property.get("type") == "title":
            return "".join(
                [t["plain_text"] for t in title_property["title"]]
            )
        return "Untitled"

# CrewAI Tools
notion_search_tool = Tool(
    name="Notion Search",
    func=NotionTools().search_database,
    description="Searches the company Notion database for relevant information"
)

notion_update_tool = Tool(
    name="Notion Update",
    func=NotionTools().update_page,
    description="Updates a Notion page with new content"
)