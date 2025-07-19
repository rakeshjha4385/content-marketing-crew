# Project Structure

<img width="600" height="800" alt="image" src="https://github.com/user-attachments/assets/944cbc0e-e105-473e-991c-b8d4859bd178" />



# Content Marketing Automation with CrewAI

This project implements a multi-agent system for automating content marketing workflows using CrewAI.

## Features

- Multi-agent collaboration for content creation
- Integration with Notion, Slack, and n8n
- Automated research, writing, editing, and publishing workflows
- Memory and context management between agents

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file based on `.env.example`
4. Run the main workflow: `python main.py`

## Workflows

1. **Blog Post Creation**
   - Research → Writing → Editing → Publishing
   
2. **Social Media Content**
   - Research → Content Creation → Approval → Scheduling

3. **Newsletter Production**
   - Content Collection → Curation → Design → Distribution

## Testing

Run tests with:
```bash
pytest tests/
```