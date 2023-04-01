from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Go to Amazon page')
def open_amazon(context):
    #context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()


@when('Click on Cart icon')
def click_orders_button(context):
    #context.driver.find_element(By.CSS_SELECTOR,'#nav-cart').click()
    context.app.header.click_cart()


@then('Text "{expected_result}" is displayed')
def verify_empty_cart(context, expected_result):
    context.app.empty.verify_empty_cart(expected_result)