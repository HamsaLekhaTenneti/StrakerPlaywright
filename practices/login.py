from dashboard import DashBoardPage

from conftest import user_credentials


class LoginPage:

    def __init__(self,page):
        self.page=page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client/auth/login")  
 
    def login(self,userEmail,userPassword):
        self.page.get_by_placeholder("email@example.com").fill(user_credentials["userEmail"])
        self.page.get_by_placeholder("enter your passsword").fill(user_credentials["userPassword"])
        self.page.get_by_role("button",name="Login").click()
        dashboardPage=DashBoardPage(self.page)
        return dashboardPage
    


    