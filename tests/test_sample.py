from playwright.sync_api import Page

BASE_URL="https://rahulshettyacademy.com"

def test_playwrightBasics(playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto(BASE_URL)   


def test_playwrightShortCut(page:Page):
    page.goto(BASE_URL)


def test_login(page:Page):
    page.goto(f"{BASE_URL}/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link",name="terms and condition").click()
    page.get_by_role('button',name="Sign in").click()






