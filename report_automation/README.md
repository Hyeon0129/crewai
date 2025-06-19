# Report Automation Crew

This project demonstrates an automated research workflow powered by [crewAI](https://crewai.com). It creates a multi-agent system that searches the web, extracts information, summarizes the findings, and generates a report in Markdown and PDF formats.

## Directory Structure

```
report_automation/
├── README.md
├── pyproject.toml
├── config/
│   ├── agents.yaml
│   └── tasks.yaml
└── src/
    └── report_automation/
        ├── __init__.py
        ├── crew.py
        ├── main.py
        └── tools/
            └── web_search.py
```

## Setup

1. Install [uv](https://docs.astral.sh/uv/):
   ```bash
   pip install uv
   ```
2. From the repository root, install dependencies:
   ```bash
   crewai install
   ```
   or use `uv` directly:
   ```bash
   uv pip install -r <(uv pip compile report_automation/pyproject.toml)
   ```

## Running

To generate a report run:

```bash
crew run report_automation
```

The program will ask for a topic and produce `report.md` and `report.pdf` in the project root.


