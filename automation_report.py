"""Automation script using crewAI agents to generate a report."""
import os
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from report_automation.src.report_automation.tools.web_search import fetch_top_results

OLLAMA_API = os.getenv('OLLAMA_API', 'http://175.124.38.106:9676/api/generate')


def call_ollama(prompt: str) -> str:
    """Call the Qwen2.5 model via Ollama API."""
    response = requests.post(OLLAMA_API, json={"model": "qwen:30b", "prompt": prompt})
    response.raise_for_status()
    return response.json().get('response', '')


def analyze_topic(topic: str) -> str:
    prompt = f"Generate short search keywords for: {topic}"
    return call_ollama(prompt)


def extract_text(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup(['style', 'script', 'header', 'footer', 'nav', 'aside']):
        tag.decompose()
    return ' '.join(soup.stripped_strings)


def summarize(text: str) -> str:
    prompt = f"Summarize the following text as bullet points:\n{text}"
    return call_ollama(prompt)


def save_markdown(content: str, filename: str) -> None:
    with open(filename, 'w') as f:
        f.write(content)


def main(topic: str):
    keywords = analyze_topic(topic)
    pages = fetch_top_results(keywords)
    texts = [extract_text(p) for p in pages]
    summary = summarize('\n'.join(texts))

    markdown = f"# {topic} Report\n\nGenerated on {datetime.now().date()}\n\n" + summary
    save_markdown(markdown, 'report.md')
    try:
        import pdfkit
        pdfkit.from_string(markdown, 'report.pdf')
    except Exception as e:
        print(f"PDF generation failed: {e}")


if __name__ == '__main__':
    import sys
    topic = sys.argv[1] if len(sys.argv) > 1 else input('Enter topic: ')
    main(topic)

