from crewai import Crew
from agents.researcher import researcher
from agents.writer import writer
from agents.editor import ContentEditor
from agents.publisher import ContentPublisher

# Initialize with your chosen LLM
writer = ContentWriter(llm=llm)
editor = ContentEditor(llm=llm)
publisher = ContentPublisher(llm=llm)

content_crew = Crew(
  agents=[researcher, writer],
  process="sequential",  # Tasks run in order
  memory=True,  # Shared context
  output_json_file="output.json"  # Auto-save results
)

result = content_crew.kickoff(inputs={"topic": "AI in Content Marketing"})
