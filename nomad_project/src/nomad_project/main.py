#!/usr/bin/env python
import sys
import warnings
import os
from pathlib import Path
from markdown import markdown
from fpdf import FPDF

from datetime import datetime

# Allow running this file directly without installing the package
if __package__ is None or __package__ == "":
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from nomad_project.crew import NomadProject

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Convert markdown report to PDF
def _md_to_pdf(md_file: str, pdf_file: str) -> None:
    """Create a simple PDF file from markdown text."""
    try:
        text = Path(md_file).read_text()
    except FileNotFoundError:
        return
    html = markdown(text)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    for line in html.splitlines():
        pdf.multi_cell(0, 10, line)
    pdf.output(pdf_file)

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    topic = sys.argv[1] if len(sys.argv) > 1 else 'AI LLMs'
    inputs = {
        'topic': topic,
        'current_year': str(datetime.now().year)
    }
    
    try:
        NomadProject().crew().kickoff(inputs=inputs)
        _md_to_pdf("report.md", "report.pdf")
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        NomadProject().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        NomadProject().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        NomadProject().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


if __name__ == "__main__":
    run()
