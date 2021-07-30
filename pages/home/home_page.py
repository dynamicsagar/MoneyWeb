import time

from base.selenium_driver import SeleniumDriver
from testcases.message import *
from selenium.webdriver.common.action_chains import ActionChains


class HomePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _main_logo = "main-logo"
    _home_side_menu_link = "Home"
    _applications_side_menu_link = ".apps"
    _account_admin_side_menu_link = ".settings"
    _developer_side_menu_link = ".fa-code"
    _docs_side_menu_link = ".docs"
    _team_toggle_drop_down = "teams-toggle"
    _sandbox_toggle_button_text = "//form[@id='sandbox-toggle']/label"
    _production_toggle_button_text = "//form[@id='sandbox-toggle']/label[2]"
    _user_menu_icon = "//div[@id='user-menu']/a/span/span[1]"
    _change_password_link = "//div[@id='user-menu']/div/a[2]"
    _profile_link = "//div[@id='user-menu']/div/a[1]"
    _logout_link = "//div[@id='user-menu']/div/a[3]"

    def clickMainLogoLink(self):
        self.wait_for_element(self._main_logo)
        self.element_click(self._main_logo)

    def clickHomeSideMenuLink(self):
        self.wait_for_element(self._home_side_menu_link)
        self.wait_for_element(self._home_side_menu_link)

    def clickApplicationSideMenuLink(self):
        self.wait_for_element(self._applications_side_menu_link)
        self.element_click(self._applications_side_menu_link)

    def clickAccountAdminSideMenuLink(self):
        self.wait_for_element(self._account_admin_side_menu_link)
        self.element_click(self._account_admin_side_menu_link)

    def clickDocsSideMenuLink(self):
        self.wait_for_element(self._docs_side_menu_link)
        self.element_click(self._docs_side_menu_link)

    def ClickTeamToggleDropDownButton(self):
        self.wait_for_element(self._team_toggle_drop_down)
        self.element_click(self._team_toggle_drop_down)

    def clickDeveloperSideMenuLink(self):
        self.wait_for_element(self._developer_side_menu_link)
        self.element_click(self._developer_side_menu_link)

    def clickMenuIcon(self):
        self.wait_for_element(self._user_menu_icon)
        self.element_click(self._user_menu_icon)

    def clickPasswordLink(self):
        self.wait_for_element(self._change_password_link)
        self.element_click(self._change_password_link)

    def clickProfileLink(self):
        self.wait_for_element(self._profile_link)
        self.element_click(self._profile_link)

    def clickLogoutLink(self):
        self.wait_for_element(self._logout_link)
        self.element_click(self._logout_link)



