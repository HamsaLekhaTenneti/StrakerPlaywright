import json
from playwright.sync_api import Page,Playwright
import pytest
from practices.login import LoginPage
from .pageObjects.orderDetails import OrderDetailsPage
from .pageObjects.dashboard import DashBoardPage
from utils.apibase import APIUtils

with open('credentials.json') as f:
        test_data=json.load(f)
        print(test_data)
        user_credentials_list=test_data['user_credentials']

@pytest.mark.parametrize('user_credentials',user_credentials_list)
def test_e2e_validations(playwright:Playwright,user_credentials):
    userName=user_credentials["userEmail"]
    userPassword=user_credentials["userPassword"]
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    api_utils=APIUtils()
    orderID=api_utils.createOrder(playwright,user_credentials)

    loginpage= LoginPage(page) 
    loginpage.navigate() 
    loginpage.login(userName,userPassword)

    dashboard=DashBoardPage(page)
    dashboard.selectOrdersNavLink()
    orderHistoryPage=DashBoardPage.selectOrdersNavLink()
    orderHistoryPage.selectOrder(orderID)
    OrderDetailsPage.verifyOrderMessage()
    context.close()


    


