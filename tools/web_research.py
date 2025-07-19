from crewai import Tool
from duckduckgo_search import ddg
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re

class WebResearchTools:
    def search_web(self, query: str, max_results: int = 5):
        """Search the web for relevant information"""
        try:
            results = ddg(query, max_results=max_results)
            return [{
                "title": r["title"],
                "url": r["link"],
                "snippet": r["body"]
            } for r in results]
        except Exception as e:
            return f"Error searching web: {str(e)}"

    def scrape_website(self, url: str):
        """Scrape content from a website"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Remove unwanted elements
            for element in soup(['script', 'style', 'nav', 'footer']):
                element.decompose()
                
            # Get clean text
            text = soup.get_text()
            text = re.sub(r'\s+', ' ', text).strip()
            
            return {
                "url": url,
                "domain": urlparse(url).netloc,
                "content": text[:5000]  # Limit content length
            }
        except Exception as e:
            return f"Error scraping website: {str(e)}"

# CrewAI Tools
web_search_tool = Tool(
    name="Web Search",
    func=WebResearchTools().search_web,
    description="Searches the web for relevant information using DuckDuckGo"
)

web_scrape_tool = Tool(
    name="Website Scraper",
    func=WebResearchTools().scrape_website,
    description="Scrapes content from a given website URL"
)