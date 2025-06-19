# crewAI Automation Example

This repository contains examples using the [crewAI](https://crewai.com) framework. The **Report Automation Crew** shows how multiple agents can research a topic and generate a final report.

## Projects

- `latest_ai_development` – template project included with crewAI.
- `report_automation` – automated web research workflow.

## Running Report Automation

Install dependencies and run the crew:

```bash
pip install uv
crewai install
crew run report_automation -- "Your topic"
```

The run creates `report.md` and `report.pdf` in the repository root.

See `report_automation/README.md` for more details.

