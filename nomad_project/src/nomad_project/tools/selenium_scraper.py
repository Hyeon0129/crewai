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
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(options=options)
        driver.get(f"https://www.google.com/search?q={query}")
    )
