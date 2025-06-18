#  Nomad Project - AI Agent Automation with CrewAI

This is a personal project exploring automation using the **CrewAI framework**, designed to experiment with multi-agent systems and local LLM integration.

##  Goals

- Automate repetitive research and documentation tasks using AI agents
- Understand and apply CrewAI's core structure (Agent, Task, Crew)
- Integrate with local LLMs such as **Ollama**, **Hermes 3**, and others
- Experiment with agent collaboration and role specialization

## 📁 Project Structure


nomad_project/
├── config/
│ ├── agents.yaml # Agent definitions
│ └── tasks.yaml # Task definitions
├── tools/ # Custom tool implementations
├── crew.py # Crew and process configuration
├── main.py # Entry point for execution

##  Getting Started

```bash
# Install CrewAI and tools
pip install crewai
pip install 'crewai[tools]'

# Create a new project (if needed)
crewai create crew nomad_project

# Run your crew
python nomad_project/main.py