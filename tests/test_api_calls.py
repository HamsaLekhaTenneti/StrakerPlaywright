from playwright.sync_api import Page,Playwright
from utils.apibase import APIUtils
from test_sample import BASE_URL


def test_e2e_validations(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    api_utils=APIUtils()
    api_utils.createOrder(playwright)
    page.goto(f"{BASE_URL}/client/auth/login")  
    page.get_by_placeholder("email@example.com").fill("hamsa@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Hamsa@123")
    page.get_by_role("button",name="Login").click()

