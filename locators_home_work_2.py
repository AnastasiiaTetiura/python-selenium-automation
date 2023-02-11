from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service


service = Service('/Users/anastasiiatetiura/PycharmProjects/Home_Work_2/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')

# Amazon logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")

# email field
driver.find_element(By.ID, 'ap_email')

# continue button
driver.find_element(By.XPATH, "//input[@aria-labelledby='continue-announce']")

# Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# forgot  password
driver.find_element(By.ID, 'auth-fpp-link-bottom')

# other issues link
driver.find_element(By.ID, 'ap-other-signin-issues-link')

# create account button
driver.find_element(By.ID, 'createAccountSubmit')

# condition link
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

# privacy notice link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

