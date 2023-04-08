from selenium.webdriver.common.by import By
from classwork_7.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    SUBNAV = (By.CSS_SELECTOR, "#nav-subnav[data-category='{CATEGORY}']")
    DEALS = (By.XPATH, '//h3[text()="Boys"]')

    def get_subnav_locator(self,categoty):
        return [self.SUBNAV[0], self.SUBNAV[1] .replace('{CATEGORY}', categoty)]

    def verify_search_result(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)

    def verify_selected_dept(self, category):
        locator = self.get_subnav_locator(category)
        print(locator)
        self.wait_for_element_appear(*locator)

    def verify_new_deals(self):
        self.wait_for_element_appear(*self.DEALS)
