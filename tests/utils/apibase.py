from playwright.sync_api import Playwright
from apiBaseFramework import ordersPayLoad, BASE_URL

class APIUtils:

    def gettoken(self,playwright:Playwright,user_credentials):
        user_email=user_credentials['userEmail']
        user_password=user_credentials['userPassword']
        api_request_context=playwright.request.new_context(base_url=BASE_URL)
        response=api_request_context.post(url="api/ecom/auth/login", data={"userEmail": user_email, "userPassword": user_password})
        assert response.ok
        print(response.json())
        responseBody = response.json()
        return responseBody["token"]


    def createOrder(self,playwright:Playwright,user_credentials):
        token=self.gettoken(playwright,user_credentials)
        api_request_context=playwright.request.new_context(base_url=BASE_URL)
        response=api_request_context.post(url="/api/ecom/order/create-order", # type: ignore
                                 data=ordersPayLoad
                                 ,headers={"Authorization": token, "content-Type":"application/json"}
                                )
        print(response.json())
                            