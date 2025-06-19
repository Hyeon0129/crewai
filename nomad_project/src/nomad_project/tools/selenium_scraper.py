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
        "Searches the web using Google and returns the page text for the first result"
    )
    args_schema: Type[BaseModel] = WebScrapeInput

    def _run(self, query: str) -> str:
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(options=options)
        driver.get(f"https://www.google.com/search?q={query}")
        link = None
        for element in driver.find_elements(By.CSS_SELECTOR, "a"):
            href = element.get_attribute("href")
            if href and href.startswith("http") and "google" not in href:
                link = href
                break
        if not link:
            driver.quit()
            return ""
        driver.get(link)
        time.sleep(2)
        text = driver.page_source
        driver.quit()
        return text
