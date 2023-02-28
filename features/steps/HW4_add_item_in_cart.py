from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Input text {text}')
def input_search_item(context, text):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(text)


@when('Click on the search button')
def click_search_button(context):
    context.driver.find_element(By.CSS_SELECTOR, '#nav-search-submit-button').click()
    sleep(1)


@when('Click on the first item')
def click_first_item(context):
    context.driver.find_element(By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]").click()
    sleep(1)


@when('Click Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-button').click()
    sleep(1)


@then('Verify has 1 item')
def verify_item_added(context):
    context.driver.find_element(By.CSS_SELECTOR, '.a-dropdown-prompt')
    sleep(1)
