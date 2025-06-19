# **Nomad Project - AI Agent Automation with CrewAI**

A personal project exploring automation using the **CrewAI** framework, focused on experimenting with multi-agent 
systems and integrating local LLMs.

---

## **Goals**
- Automate repetitive research and documentation tasks using AI agents  
- Understand and apply CrewAI's core structure: **Agent**, **Task**, **Crew**  
- Integrate with local LLMs such as **Ollama**, **Hermes 3**, and others  
- Experiment with agent collaboration and role specialization  



## **Project Structure**
```
nomad_project/
├── config/                # Configuration files
│   ├── agents.yaml        # Agent definitions
│   └── tasks.yaml         # Task definitions
├── tools/                 # Custom tool implementations
├── crew.py                # Crew and process configuration
└── main.py                # Entry point for execution
```



## **Getting Started**

### **1. Install Dependencies**
```bash
# Install CrewAI and required tools
pip install crewai
pip install 'crewai[tools]'
pip install selenium beautifulsoup4

# Set your local LLM API endpoint
export OPENAI_API_BASE=http://175.124.38.106:9676/
```

### **2. Create a New Project (Optional)**
```bash
# Use CrewAI CLI to create a new project (if needed)
crewai create crew nomad_project
```

### **3. Run the Crew**
```bash
# Execute the project
python nomad_project/main.py
# Provide a topic to run a web-scraping report
python nomad_project/main.py "your topic here"
```

---

## **Key Features**
- **Multi-agent collaboration**: Design workflows where agents specialize in roles (e.g., Researcher, Writer, Editor). 
- **Local LLM integration**: Leverage models like Ollama or Hermes 3 for lightweight, on-device processing.  
- **Custom tool support**: Extend functionality with tools for data collection, API calls, or document generation.  
- **Modular architecture**: Easily swap agents, tasks, or tools to experiment with different automation scenarios.  



## **Example Workflow**
1. **Researcher** gathers data on a topic.  
2. **Writer** compiles the data into a draft document.  
3. **Editor** reviews and refines the content.  
4. **Final Output** is generated as a polished document.  

