from selenium.webdriver.common.by import By
from classwork_7.base_page import Page
from time import sleep


class EmptyCart(Page):
    CART_IS_EMPTY = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2")

    def verify_empty_cart(self, expected_text):
        self.verify_text(expected_text, *self.CART_IS_EMPTY)

