from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Amazon page')
def open_amazon(context):
    #context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()


@when('Click on Orders button')
def click_orders_button(context):
    #context.driver.find_element(By.XPATH,"//span[text()='& Orders' and @class='nav-line-2']").click()
    context.app.header.click_orders()


@then('Page Sing In is open')
def verify_sign_in(context):
    #context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")
    context.app.main_page.verify_page_url("https://www.amazon.com/ap/signin")


