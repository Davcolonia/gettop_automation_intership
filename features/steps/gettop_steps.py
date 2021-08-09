from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep, time



@given('Open Gettop store')
def open_gettop(context):
    context.driver.get('https://gettop.us/')

@given('Go to product ipad')
def goto_product_gettop(context):
    context.driver.get('https://gettop.us/product/ipad/')

@when('User clicks on cart icon')
def click_cart(context):
    context.driver.find_element(By.XPATH, "//span[@class='cart-icon image-icon']").click()

@when('User hovers cart icon')
def click_cart(context):
    if __name__ == '__main__':
        context.driver.find_element(By.XPATH, "//span[@class='cart-icon image-icon']").text


@when('Click on the Add to cart button in bottom')
def click_cart(context):
    context.driver.find_element(By.XPATH, "//button[@class='single_add_to_cart_button button alt']").click()

@when('click on view cart')
def click_cart(context):
    context.driver.find_element(By.XPATH,"//p[@class='woocommerce-mini-cart__buttons buttons']//a[contains(@href,'https://gettop.us/cart/')]").click()


@when('click on checkout')
def click_cart(context):
    context.driver.find_element(By.XPATH,"//p[@class='woocommerce-mini-cart__buttons buttons']//a[contains(@href,'https://gettop.us/checkout/')]").click()


@when('click on remove items')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,"a.remove.remove_from_cart_button").click()

@then("Verify dropdown price {expected_price}")
def verify_menu_price(context, expected_price):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='woocommerce-Price-amount amount']").text
    assert actual_result == expected_price, f'Expected {expected_price} but got {actual_result}'
        #context.app.search_results_page.verify_search_worked(expected_text)

@then("Verify expected product")
def verify_menu_price(context):
    expected_product = context.driver.find_element(By.XPATH, "//a[@href='https://gettop.us/product/ipad/']").text
    #assert actual_result == expected_quantity, f'Expected {expected_quantity} but got {actual_result}'
        #context.app.search_results_page.verify_search_worked(expected_text)

@then("Verify {expected_text} item in the nav menu")
def verify_menu_price(context, expected_text):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='cart-icon image-icon']").text
    assert actual_result == expected_text, f'Expected {expected_text}, but got {actual_result}'
        #context.app.search_results_page.verify_search_worked(expected_text)

@then("Verify price {expected_text} in the nav menu")
def verify_menu_price(context, expected_text):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'span.cart-price').text
    assert actual_result == expected_text, f'Expected {expected_text}, but got {actual_result}'
        #context.app.search_results_page.verify_search_worked(expected_text)

@then("{expected_text} is displayed")
def verify_empty_cart(context, expected_text):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'p.cart-empty').text
    assert actual_result == expected_text, f'Expected {expected_text}, but got {actual_result}'
        #context.app.search_results_page.verify_search_worked(expected_text)

@then("No products in the cart is shown")
def verify_empty_cart(context):
    context.driver.find_element(By.XPATH, "//li[@class='html widget_shopping_cart']").text
    #assert actual_result == expected_text, f'Expected {expected_text}, but got {actual_result}'
        #context.app.search_results_page.verify_search_worked(expected_text)

@then("Verify items in cart page")
def verify_empty_cart(context):
    context.driver.find_element(By.XPATH, "//tr[@class='woocommerce-cart-form__cart-item cart_item']//a[contains(@href,'https://gettop.us/product/ipad/')]").text
    #assert actual_result == expected_text, f'Expected {expected_text}, but got {actual_result}'
        #context.app.search_results_page.verify_search_worked(expected_text)

@then("Verify checkout page")
def verify_empty_cart(context):
    context.driver.find_element(By.XPATH,"//td[@class='product-name']").text
    #assert actual_result == expected_text, f'Expected {expected_text}, but got {actual_result}'
        # context.app.search_results_page.verify_search_worked(expected_text)

@then("Verify no items")
def verify_empty_cart(context):
    context.driver.find_element(By.XPATH, "//p[@class='woocommerce-mini-cart__empty-message']").text
        # assert actual_result == expected_text, f'Expected {expected_text}, but got {actual_result}'
        # context.app.search_results_page.verify_search_worked(expected_text)

