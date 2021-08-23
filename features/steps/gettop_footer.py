from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep, time


@then('Verify {expected_cat} Best Selling, Latest, Top Rated categories')
def verify_footer_links_amount(context, expected_cat):
    cat_count = context.driver.find_elements(By.CSS_SELECTOR, "span.widget-title")
    print(cat_count)
    print('\nAmount: ', len(cat_count))
    assert len(cat_count) == expected_cat, f'Expected 3 categories, but got {len(cat_count)}'


@then('Verify price option in footer')
def verify_footer_links_amount(context):
    context.driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.product-title")))


@then('Verify name option in footer')
def verify_footer_links_amount(context):
    context.driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.star-rating")))


@then('Verify star rating option in footer')
def verify_footer_links_amount(context):
    context.driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.woocommerce-Price-amount.amount")))


@then('Verify {text} in footer')
def verify_footer_links_amount(context, text):
  actual_text = context.driver.find_element(By.CSS_SELECTOR, "div.copyright-footer").text
  assert actual_text == text.lower(), f'Expected {text}, but got {actual_text}'

@then('Verify button to go back to top')
def verify_footer_links_amount(context):
    context.driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "i.icon-angle-up")))

@when('User can click footer link for iphone')
def click_cart(context):
    context.app.header.click_footer_phone()

@when('User can click footer link for mac')
def click_cart(context):
    context.app.header.click_footer_mac()

@when('User can click footer link for watch')
def click_cart(context):
    context.app.header.click_footer_watch()


@when('User can click footer link for ipad')
def click_cart(context):
    context.app.header.click_footer_iPad()


@when('User can click footer link for accessories')
def click_cart(context):
    context.app.header.click_footer_accessory()
