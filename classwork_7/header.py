from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from classwork_7.base_page import Page


class Header(Page):
    LANG_OPTIONS = (By.ID, 'icp-nav-flyout')
    SPANISH_LANG = (By.CSS_SELECTOR, 'a[href="#switch-lang=es_US"]' )
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    ORDERS = (By.XPATH,"//span[text()='& Orders' and @class='nav-line-2']")
    CART = (By.ID,"nav-cart-count-container")
    DEPARTMENT_SELECTION = (By.ID, 'searchDropdownBox')
    NEW_ARR = (By.XPATH, '//span[text()="New Arrivals"]')
    DEALS = (By.XPATH, '//h3[text()="Boys"]')

    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_orders(self):
        self.click(*self.ORDERS)

    def click_cart(self):
        self.click(*self.CART)

    def hover_lang_options(self):
        lang_options = self.find_element(*self.LANG_OPTIONS)
        actions = ActionChains(self.driver)
        actions.move_to_element(lang_options)
        actions.perform()

    def verify_lang_shown(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

    def select_department(self, alias):
        department_dd = self.find_element(*self.DEPARTMENT_SELECTION)
        select = Select(department_dd)
        select.select_by_value(f'search-alias={alias}')

    def hover_over_arrivals(self):
        new_arrivals_options = self.find_element(*self.NEW_ARR)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals_options)
        actions.perform()

