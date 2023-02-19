from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


#SEARCH_INPUT = (By.NAME, 'q')
#SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    sleep(1)


@when('Click on Orders button')
def click_orders_button(context):
    context.driver.find_element(By.XPATH,"//span[text()='& Orders' and @class='nav-line-2']").click()
    sleep(1)


@then('Text Sing In is shown')
def verify_sign_in(context):
    context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")




