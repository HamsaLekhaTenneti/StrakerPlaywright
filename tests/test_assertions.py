import time
from playwright.sync_api import Page,expect


def test_asssertionsvalidation(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role(role="button",name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    
def test_handlepopup(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.on("dialog",lambda x:x.accept())
    page.get_by_role("button",name="Confirm").click()
    time.sleep(5)

def test_handlingframes(page:Page):
     page.goto("https://rahulshettyacademy.com/AutomationPractice/")
     pageFrame=page.frame_locator("#courses-iframe")
     pageFrame.get_by_role("link",name="All Access plan").click()
     expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")

def test_UIvalidations(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator("th")).count():
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            priceColvalue= index
            print(f"price col value is {priceColvalue}")
            break
    riceRow=page.locator("tr").filter(has_text="Rice")
