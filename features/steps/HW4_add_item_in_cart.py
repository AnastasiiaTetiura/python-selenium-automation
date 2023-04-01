from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART = (By.ID, 'nav-cart-count')
PRODUCT_NAME = (By.ID, 'productTitle')
PRODUCT_PRICE = (By.ID, 'corePrice_feature_div')


@when('Click on the first item')
def click_first_item(context):
    context.driver.find_element(By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]").click()
    sleep(1)


@when('Click Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-button').click()
    sleep(1)


@when('Store product name and price')
def get_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.product_name}')
    context.product_price = context.driver.find_element(*PRODUCT_PRICE).text
    print(f'Current product price: {context.product_price}')


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_text = context.driver.find_element(*CART).text
    assert expected_count == actual_text, f'Expected {expected_count}, but got {actual_text}'



#@then('Verify cart has correct product and price')
#def verify_product_name(context):
    #actual_name = context.driver.find_element(*PRODUCT_NAME).text
    #assert context.product_name[:15] in actual_name, f'Expected {context.product_name} but got {actual_name}'

    #actual_price = context.driver.find_element(*PRODUCT_PRICE).text
    #assert context.product_price == actual_price, f'Expected {context.product_price} but got {actual_price}'