from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

HEADER_LINKS = (By.CSS_SELECTOR, 'a[href*="ref=zg_bs_tab"]')


@when('Select hamburger manu')
def select_hamburger_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, '#nav-hamburger-menu').click()
    sleep(1)


@when('Select Best Sellers in dropdown')
def select_best_sellers(context):
    context.driver.find_element(By.CSS_SELECTOR, '#hmenu-content a[href*="/gp/bestsellers/"]').click()
    sleep(1)


@then('Verify header has {expected_amount} links')
def verify_header_links(context, expected_amount):
    expected_amount = int(5)
    header_links = context.driver.find_elements(*HEADER_LINKS)
    assert len(header_links) == expected_amount, f'Expected {expected_amount} links but got {len(header_links)}'
