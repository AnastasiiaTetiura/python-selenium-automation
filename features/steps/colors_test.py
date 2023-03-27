from behave import step
from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

COLORS = (By.ID, '#variation_color_name li')
CUR_COLOR = (By.CSS_SELECTOR,'#variation_color_name .selection')


@given('Open Amazon product {product_id} page')
def open_amazon_page(context, product_id):
    context.driver.get('https://www.amazon.com/Amazon-Essentials-Womens-Solid-Surplice/dp/{product}/')


@then('User can click  color options')
def click_color(context):
    context.driver.find_element(*COLORS).click()

    all_color_option = context.driver.find_elements(*COLORS)
    expected_colors = ['Black',  'Burgundy',  'Navy', 'Black, Confetti'] #it is exactly form the Amazon result as one color option 'Black, Confetti'

    actual_colors = []
    for color in all_color_option:
        color.click()
        cur_color = context.driver.find_element(*CUR_COLOR).text
        print('Current color: ', cur_color)
        actual_colors += [cur_color]

    assert expected_colors == actual_colors, f'expected {expected_colors}, but got {actual_colors}'
