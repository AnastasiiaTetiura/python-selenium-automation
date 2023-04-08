from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep


@when('Select department by alias {alias}')
def select_department(context, alias):
    context.app.header.select_department(alias)


@then('Verify {category} department is selected')
def verify_selected_dept(context, category):
    context.app.search_results.verify_selected_dept(category)

