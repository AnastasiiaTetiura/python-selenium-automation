from selenium.webdriver.common.by import By
from classwork_7.base_page import Page


class SigninPage(Page):
    def verify_signin_opened(self):
        self.verify_page_url('https://www.amazon.com/ap/signin')
