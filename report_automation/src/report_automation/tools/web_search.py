import time
from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def fetch_top_results(query: str, num_results: int = 5) -> List[str]:
    """Search the web and return HTML of top results."""
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(f'https://www.google.com/search?q={query}')
        links = driver.find_elements(By.CSS_SELECTOR, 'a')
        urls = []
        for link in links:
            href = link.get_attribute('href')
            if href and href.startswith('http') and 'google' not in href:
                urls.append(href)
            if len(urls) >= num_results:
                break
        pages = []
        for url in urls:
            driver.get(url)
            time.sleep(1)
            pages.append(driver.page_source)
        return pages
    finally:
        driver.quit()

from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class SearchInput(BaseModel):
    query: str = Field(..., description="Search query")

class WebSearchTool(BaseTool):
    name: str = "web_search"
    description: str = "Search the web and return HTML of top results"
    args_schema: Type[BaseModel] = SearchInput

    def _run(self, query: str) -> list:
        return fetch_top_results(query)

class ExtractInput(BaseModel):
    html: str = Field(..., description="HTML content")

class ExtractTextTool(BaseTool):
    name: str = "extract_text"
    description: str = "Extract main text from HTML"
    args_schema: Type[BaseModel] = ExtractInput

    def _run(self, html: str) -> str:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        for tag in soup(['style', 'script', 'header', 'footer', 'nav', 'aside']):
            tag.decompose()
        return ' '.join(soup.stripped_strings)
