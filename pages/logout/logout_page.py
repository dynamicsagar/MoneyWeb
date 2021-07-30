import time

from pages.home.home_page import HomePage
from base.selenium_driver import SeleniumDriver
from testcases.message import *


class LogoutPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.home = HomePage(driver)

    # Locators
    _close_icon = "//div[@id='logout-modal']/div/div/button/span"
    _cancel_button = "//button[contains(text(),'Cancel')]"
    _logout_button = "//button[contains(text(),'Logout')]"
    _popup_text = '''//div[contains(text(),'Select "Logout" below if you are ready to end your')]'''
    _popup_title = "//div[@id='logout-modal-title']"

    def getPopupTitle(self):
        self.wait_for_element(self._popup_title)
        return self.get_text(self._popup_title)

    def getPopText(self):
        self.wait_for_element(self._popup_text)
        return self.get_text(self._popup_text)

    def clickCloseIcon(self):
        self.wait_for_element(self._close_icon)
        self.element_click(self._close_icon)

    def clickCancelButton(self):
        self.wait_for_element(self._cancel_button)
        self.element_click(self._cancel_button)

    def clickLogoutButton(self):
        self.wait_for_element(self._logout_button)
        self.element_click(self._logout_button)

    def clickLogoutLinkFromUserMenu(self):
        self.home.clickMenuIcon()
        self.home.clickLogoutLink()

    def logout(self):
        self.clickLogoutLinkFromUserMenu()
        self.clickLogoutButton()

    # Assertions
    def verifyPopupTitle(self):
        self.clickLogoutLinkFromUserMenu()
        text = self.getPopupTitle()
        self.verify_text_match(text, popup_title)

    def verifyPopupText(self):
        text = self.getPopText()
        self.verify_text_match(text, popup_text)

    def verifyCloseIcon(self):
        self.clickCloseIcon()
        self.is_element_displayed(self.home._user_menu_icon)

    def verifyCancelButton(self):
        self.clickLogoutLinkFromUserMenu()
        self.clickCancelButton()
        self.is_element_displayed(self.home._user_menu_icon)

    def verifyLogoutSuccessfully(self):
        self.logout()
