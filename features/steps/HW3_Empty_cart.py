from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Go to Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    sleep(2)



@when('Click on Cart icon')
def click_orders_button(context):
    context.driver.find_element(By.CSS_SELECTOR,'#nav-cart').click()
    sleep(2)


@then('Text Your cart is empty is displayed')
def verify_empty_cart(context):
    context.driver.find_element(By.XPATH, '//div[@class="a-row sc-your-amazon-cart-is-empty"]')
    sleep(1)