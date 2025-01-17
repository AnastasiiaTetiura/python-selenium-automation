from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


PRIVACY_NOTICE_LINK = (By.CSS_SELECTOR, 'a.help-display-cond[href*="privacy"]')



@given('Navigate to Terms and Conditions page')
def open_tc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_current_window(context):
   context.original_window = context.driver.current_window_handle
   print(context.original_window)


@when('Click on Amazon Privacy Notice link')
def click_notice_link(context):
    context.driver.find_element(*PRIVACY_NOTICE_LINK).click()


@when('Switch to the newly opened window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    print('\nALL Windows: ',windows)
    context.driver.switch_to.window(windows[1])

    #context.current_window = context.driver.current_window_handle
    #print('\nAFTER SWITCHED')
    #print(context.current_window)


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_page_is_open(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html?nodeId'))


@then('User can close new window and switch back to original')
def close_the_window(context):
    context.driver.close()
    print('\nPrivacy page is closed')

    context.driver.switch_to.window(context.original_window)
    print('\nReturn to Original Page')


#@then('Return to original')
#def return_to_original_window(context):
    #context.driver.switch_to.window(context.original_window)


