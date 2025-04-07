import pytest
from playwright.sync_api import sync_playwright,TimeoutError 


BASE_URL = "https://www.straker.ai"
DEFAULT_TIMEOUT_MILLISECONDS = 60000

@pytest.fixture(scope="function")
def launchbrowser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        # Headless True is default which will not launch browser
        context = browser.new_context()
        page = context.new_page()
        # Reference: https://playwright.dev/python/docs/api/class-frame#frame-wait-for-selector
        try:
          page.goto(BASE_URL, wait_until="domcontentloaded")
          yield page # Before this is @BeforeTest and After this is @AfterTest
        except TimeoutError:
           print("Timeouterror")
        browser.close()