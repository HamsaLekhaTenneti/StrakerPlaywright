from playwright.sync_api import expect, Page
from test_fixtures import launchbrowser, BASE_URL,DEFAULT_TIMEOUT_MILLISECONDS

def test_navigate_to_tiri_page(launchbrowser: Page):

    page=launchbrowser

    # Hovering over "Products"
    product_link = page.get_by_role("button", name="Products")
    expect(product_link).to_be_visible(timeout=DEFAULT_TIMEOUT_MILLISECONDS)
    product_link.hover()

    # Clicking "Learn More" under Tiri
    tiri_learnmore = page.locator("xpath=//a[@class='learn_more-tiri w-inline-block']//div[contains(text(),'Learn More')]")
    tiri_learnmore.wait_for(state="visible", timeout=DEFAULT_TIMEOUT_MILLISECONDS)
    tiri_learnmore.click()

    # Assert that the Tiri page is loaded by TEXT
    expect(page.locator("h1", has_text="Tiri")).to_be_visible(timeout=DEFAULT_TIMEOUT_MILLISECONDS)
    # page.wait_for_selector("text=Tiri", timeout=DEFAULT_TIMEOUT_MILLISECONDS)
    # Assert the page by URL
    expect(page).to_have_url(f"{BASE_URL}/products/tiri", timeout=DEFAULT_TIMEOUT_MILLISECONDS)
