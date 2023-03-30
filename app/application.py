from classwork_7.main_page import MainPage
from classwork_7.header import Header
from classwork_7.search_results import SearchResultsPage
from classwork_7.sign_in_page import SigninPage
from classwork_7.empty import EmptyCart


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.sign_in_page = SigninPage(self.driver)
        self.empty = EmptyCart(self.driver)




