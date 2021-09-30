"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import os

from selenium import webdriver
from testcases.test_config import *
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self, env):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """

        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        else:
            # Set chrome driver
            # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
            # chromedriver = "./drivers/chromedriver.exe"
            # os.environ["webdriver.chrome.driver"] = driver
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--incognito")
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
            driver.implicitly_wait(30)
            driver.set_window_size(1440, 900)
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        if env == 'stage':
            baseURL = stage_url
            driver.get(baseURL)
        elif env == 'prod':
            baseURL = production_url
            driver.get(baseURL)
        elif env == 'dev':
            baseURL = dev_url
            driver.get(baseURL)
        else:
            baseURL = stage_url
            driver.get(baseURL)
        return driver
