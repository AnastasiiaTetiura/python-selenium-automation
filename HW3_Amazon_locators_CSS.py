#Home_work 3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(executable_path='/Users/anastasiiatetiura/Desktop/A-Tet/CARRERIST/git_rep/python-selenium-automation/chromedriver')

# Amazon logo
driver.find_element(By.CSS_SELECTOR, 'a.a-link-nav-icon')

# Create Account
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# your name field
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

# email field
driver.find_element(By.CSS_SELECTOR, '#ap_email')

# password field
driver.find_element(By.CSS_SELECTOR, '#ap_password')

# re-enter field
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

# create Amazon button
driver.find_element(By.CSS_SELECTOR, 'input.a-button-input')

# Condition of use
#NOTE - I tried to make it shorter by including only partiol characters
# from href, but it didn't work in Chrome dev tools
# unless I typed the whole link
driver.find_element(By.CSS_SELECTOR, '#legalTextRow a[href="/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088"]')

# Privacy Notice
driver.find_element(By.CSS_SELECTOR, '#legalTextRow a[href="/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496"]')

# Sing in
driver.find_element(By.CSS_SELECTOR, 'a[href*="/ap/signin?showRmrMe=1&openid.pape.max_auth_age=0&openid.identity"]')