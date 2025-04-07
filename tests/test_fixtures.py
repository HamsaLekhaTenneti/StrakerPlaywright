import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://www.straker.ai"
DEFAULT_TIMEOUT_MILLISECONDS = 30000

@pytest.fixture(scope="function")
def launchbrowser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(BASE_URL)
        page.wait_for_load_state("networkidle")
        yield page
        browser.close()