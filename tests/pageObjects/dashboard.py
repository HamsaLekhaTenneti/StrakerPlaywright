from playwright.sync_api import Page

class DashBoardPage:

    def __init__(self,page: Page):
        self.page=page

    def selectOrdersNavLink(self):
        self.page.get_by_role('button',name="ORDERS").click()

