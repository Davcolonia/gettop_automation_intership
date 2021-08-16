from pages.base_page import Page
from selenium.webdriver.common.by import By

class Main(Page):
    def open_main(self):
        self.open_url(url='https://amazon.com/')

    def open_gettop(self):
        self.open_url(url='https://gettop.us/shop/?orderby=menu_order')

