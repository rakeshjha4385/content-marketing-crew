# Project Structure

content-marketing-crew/
├── agents/
│   ├── researcher.py          # Research agent (web/data gathering)
│   ├── writer.py              # Content writer agent
│   ├── editor.py              # Quality control agent
│   └── publisher.py           # Handles Slack/Notion integrations
├── workflows/
│   └── content_workflow.py    # Main CrewAI workflow orchestration
├── tools/
│   ├── notion_api.py          # Notion API wrapper
│   ├── slack_notify.py        # Slack webhook tool
│   └── n8n_integration.py     # n8n automation hooks
├── data/
│   └── research_context.json  # Example memory/context storage
├── prompts/
│   ├── research.md            # Role-specific prompts
│   ├── writing.md
│   └── editing.md
├── tests/
│   └── test_agents.py         # Edge case testing
├── .env                       # API keys (excluded in .gitignore)
├── requirements.txt           # Python dependencies
└── README.md                  # Project docs + setup guide


# AI Content Marketing Crew

A CrewAI project automating content creation with:
- Research → Writing → Editing → Publishing  
- Integrations: OpenAI (GPT-4), Notion, Slack, n8n  

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
