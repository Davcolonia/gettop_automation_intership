from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep, time

@given('Open Gettop product page')
def open_gettop_products(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_gettop()

@when('User clicks sort by price')
def sort_by_price_gettop(context):
    context.app.header.click_sort()


@when('User can click through pages')
def click_through_page(context):
    context.app.header.click_pages()

@then('url opens with pages sorted by {expected_text}')
def verify_url_rating_sort(context, expected_text):
    actual_result = context.driver.current_url
    actual_result = actual_result.split("/")[-1]
    actual_result = actual_result[len("?orderby="):]

    #actual_result = context.driver.find_element(By.CSS_SELECTOR, "form.woocommerce-ordering option").text
    assert actual_result == expected_text.lower(), f'Expected {expected_text}, but got {actual_result}'
    # context.app.search_results_page.verify_search_worked(expected_text)

@when('User clicks footer link')
def click_cart(context):
    context.app.header.click_footer_phone()


@then('url opens with expected product {expected_text}')
def verify_url_rating_footer(context, expected_text):
    actual_result = context.driver.current_url
    actual_result = actual_result.split("/")[4]
    #print(actual_result)
    #actual_result = actual_result[len("iphone"):]
    assert actual_result == expected_text.lower(), f'Expected {expected_text}, but got {actual_result}'
    # context.app.search_results_page.verify_search_worked(expected_text)