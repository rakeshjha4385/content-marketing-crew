import requests
import os
from dotenv import load_dotenv

load_dotenv()

class N8nIntegration:
    @staticmethod
    def trigger_workflow(payload):
        """Trigger an n8n workflow via webhook"""
        webhook_url = os.getenv('N8N_WEBHOOK_URL')
        api_key = os.getenv('N8N_API_KEY')
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        
        response = requests.post(
            webhook_url,
            json=payload,
            headers=headers
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"n8n integration failed: {response.text}")

# CrewAI Tool
n8n_trigger_tool = Tool(
    name="Trigger n8n Workflow",
    func=N8nIntegration.trigger_workflow,
    description="Triggers an n8n workflow with the provided payload"
)