from playwright.sync_api import Page, expect
from test_sample import BASE_URL, test_login

def test_coreLocators(page:Page):
    test_login(page)
    iphone_product= page.locator("app-card").filter(has_text="iphone X")
    iphone_product.get_by_role("button").click()
    nokia_product= page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_product.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    # expect(page.locator("media-body")).to_have_count(2)








