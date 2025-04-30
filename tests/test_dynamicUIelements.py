from playwright.sync_api import Page, expect
from test_sample import BASE_URL, test_login

def locator(page:Page,text:str):
    product= page.locator("app-card").filter(has_text=text)
    product.get_by_role("button").click()


def test_coreLocators(page:Page):
    test_login(page)
    locator(page,"iphone X")
    locator(page,"Nokia Edge")
    page.get_by_text("Checkout").click()
    # expect(page.locator("media-body")).to_have_count(2)


def test_childWindowHandle(page:Page):
    page.goto(f"{BASE_URL}/loginpagePractise/")
    with page.expect_popup() as newPage_info:
        page.locator(".blinkingText").click()
        childPage=newPage_info.value
        text=childPage.locator(".red").text_content()
        print(text)
