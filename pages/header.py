from pages.base_page import Page
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    SORT_BUTTON_RATING =  (By.XPATH, "//option[@value='rating']")
    # SEARCH_ICON = (By.ID, 'nav-orders')
    # SEARCH_ICON = (By.ID, 'nav-cart')
    CART = (By.ID, 'nav_cart_count')
    CART_ICON = (By.XPATH, "//span[@class='cart-icon image-icon']")
    FLAG = (By.CSS_SELECTOR, 'icp-nav-flag.icp-nav-flag-us')
    SPANISH_LANG = (By.CSS_SELECTOR, "a[href='#switch-lang=es_US']")
    DEPARTMENT_SELECT = (By.ID, 'searchDropdownBox')
    PAGES_GETTOP = (By.XPATH, "//a[@href='https://gettop.us/shop/page/2/?orderby=rating']")



    def input_search_word(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_sort(self):
        self.click(*self.SORT_BUTTON_RATING)

    def click_pages(self):
        self.click(*self.PAGES_GETTOP)

    def verify_cart_count(self, expected_count: str):
        self.verify_text(expected_count, *self.CART)

    def hover_rating_sort(self):
        cart = self.find_element(*self.CART_ICON)
        actions = ActionChains(self.driver)
        actions.move_to_element(cart)
        actions.perform()

    def hover_flag_icon(self):
        flag = self.find_element(*self.FLAG)
        actions = ActionChains(self.driver)
        actions.move_to_element(flag)
        actions.perform()

    def verify_spanish_language_flag(self):
        self.wait_for_element_to_appear(*self.SPANISH_LANG)

    def select_department(self, alias):
        select = Select(self.find_element(*self.DEPARTMENT_SELECT))
        select.select_by_value(f'search-alias={alias}')

