from __future__ import annotations

from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


class WebScrapeInput(BaseModel):
    """Input schema for SeleniumScraperTool."""
    query: str = Field(..., description="Search query")


class SeleniumScraperTool(BaseTool):
    name: str = "Selenium Scraper"
    description: str = (
        "Searches the web using Google and returns page text from the top results"
    )
    args_schema: Type[BaseModel] = WebScrapeInput

    def _run(self, query: str, num_results: int = 5) -> str:
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(options=options)
        driver.get(f"https://www.google.com/search?q={query}")
        links = []
        for element in driver.find_elements(By.CSS_SELECTOR, "a"):
            href = element.get_attribute("href")
            if href and href.startswith("http") and "google" not in href:
                links.append(href)
            if len(links) >= num_results:
                break

        contents = []
        for url in links:
            try:
                driver.get(url)
                time.sleep(2)
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);"
                )
                time.sleep(1)
                contents.append(driver.page_source)
            except Exception:
                continue

        driver.quit()
        return "\n\n".join(contents)

