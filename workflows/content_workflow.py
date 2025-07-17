from crewai import Crew
from agents.researcher import researcher
from agents.writer import writer

content_crew = Crew(
  agents=[researcher, writer],
  process="sequential",  # Tasks run in order
  memory=True,  # Shared context
  output_json_file="output.json"  # Auto-save results
)

result = content_crew.kickoff(inputs={"topic": "AI in Content Marketing"})