from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from selenium.webdriver.support.events import EventFiringWebDriver

from app.application import Application
from support.logger import logger, MyListener

# Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
bs_user = 'davidcolonia_CgYSX3'
bs_pw = 'NkBCBpCVp4SxXxryWspx'

def browser_init(context):
    """
    :param context: Behave context
    """
    context.driver = webdriver.Chrome('/Users/hdl32da01/python-selenium-automation/chromedriver.exe')
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    # ### HEADLESS MODE ####
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    context.driver = webdriver.Chrome(chrome_options=options)

    ### EventFiringWebDriver - log file ###
    ### for drivers ###
    context.driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())
    #for headless mode
    #context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options=options), MyListener())



    # context.driver.maximize_window()
    # context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
