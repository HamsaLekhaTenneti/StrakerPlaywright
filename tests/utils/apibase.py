from playwright.sync_api import Playwright


class APIUtils:
    def gettoken(self,playwright:Playwright):
        api_request_context=playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response=api_request_context.post(url="api/ecom/auth/login", 
                                          data={"userEmail": "hamsa@gmail.com", "userPassword": "Anitha@1972"})
        assert response.ok
        print(response.json())
        responseBody = response.json()
        return responseBody["token"]




        

    def createOrder(self,playwright:Playwright):
        token=self.gettoken()
        api_request_context=playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response=api_request_context.post(url:"/api/ecom/order/create-order", # type: ignore
                                 data=orderspayload
                                 ,headers={"Authorization":token,
                                           "content-Type":"application/json"}
                                )
        print(response.json())
                            