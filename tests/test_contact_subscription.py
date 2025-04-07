from playwright.sync_api import expect, Page
from test_fixtures import launchbrowser, BASE_URL, DEFAULT_TIMEOUT_MILLISECONDS


def test_subscribe_to_updates(launchbrowser: Page):

    page=launchbrowser

    # Click Contact Button
    contact_button=page.locator("xpath=//div[@id='w-node-_28a674b5-f0a6-bbdc-a887-431fc1fc6ab4-71f10bae']")
    expect(contact_button).to_be_visible(timeout=DEFAULT_TIMEOUT_MILLISECONDS)
    contact_button.click()
    
    # Scrolling till I find Email Input Box
    email = page.locator("xpath=//input[@id='email-2']")
    # email.scroll_into_view_if_needed()  
    email.wait_for(state="visible", timeout=DEFAULT_TIMEOUT_MILLISECONDS)

    # Entered mailId and clicked on subscribe
    email.fill("test_candidate_tenneti@example.com")
    subscribe= page.locator("xpath=//input[@value='Subscribe']")
    expect(subscribe).to_be_visible(timeout=DEFAULT_TIMEOUT_MILLISECONDS)
    subscribe.click()

    # Using assertion to verify if subscription is success
    expect(page.locator("xpath=//div[@aria-label='Email Form success']//div[1]", has_text="You're successfully subscribed!")).to_be_visible(timeout=DEFAULT_TIMEOUT_MILLISECONDS)
    expect(page).to_have_url(f"{BASE_URL}/contact",timeout=DEFAULT_TIMEOUT_MILLISECONDS)