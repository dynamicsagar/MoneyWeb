import time

from base.selenium_driver import SeleniumDriver
from pages.register.register_page import RegisterPage
from pages.login.login_page import LoginPage
from testcases.message import *


class TeamCreationPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.register = RegisterPage(driver)
        self.login = LoginPage(driver)

    # Locators
    _team_dropdown_button = "//button[@id='teams-toggle']"
    _new_team_link = "//a[contains(.,' New team')]"
    _create_a_new_team_title = "//div[@id='team-modal-title']"
    _close_icon = "//span[contains(text(),'×')]"
    _enter_team_name_input_box = "//input[@id='createTeamForm.team_name']"
    _cancel_button = "//button[contains(text(),'Cancel')]"
    _create_team_button = "//button[contains(text(),'Create team')]"

    def get_team_title(self):
        return self.get_text(self._create_a_new_team_title)

    def get_team_name(self):
        return self.get_text(self._team_dropdown_button)

    def click_team_dropdown(self):
        self.wait_for_element(self._team_dropdown_button)
        self.element_click(self._team_dropdown_button)

    def click_new_team_link(self):
        self.wait_for_element(self._new_team_link)
        self.element_click(self._new_team_link)

    def click_close_icon(self):
        self.wait_for_element(self._close_icon)
        self.element_click(self._close_icon)

    def click_cancel_button(self):
        self.wait_for_element(self._cancel_button)
        self.element_click(self._cancel_button)

    def click_create_team_button(self):
        self.element_click(self._create_team_button)

    def enter_team_name(self, team_name):
        self.element_click(self._enter_team_name_input_box)
        self.send_keys(clear_field, self._enter_team_name_input_box)
        self.send_keys(team_name, self._enter_team_name_input_box)

    # Method

    def open_team_modal_box(self):
        self.click_team_dropdown()
        self.click_new_team_link()

    def create_new_team(self, team_name=''):
        self.open_team_modal_box()
        self.enter_team_name(team_name)
        time.sleep(2)
        self.click_create_team_button()

    # Assertions

    def verify_team_modal_title(self):
        self.open_team_modal_box()
        title = self.get_team_title()
        self.verify_text_match(title, TEAM_MODAL_BOX_TITLE)

    def verify_close_icon_close_the_team_modal_box(self):
        self.click_close_icon()
        self.register.welcome_screen_text()

    def verify_cancel_button_close_the_team_modal_box(self):
        self.open_team_modal_box()
        self.click_cancel_button()
        self.register.welcome_screen_text()

    def verify_create_team_button_disable(self):
        self.open_team_modal_box()
        self.check_element_state(self._create_team_button, element_name='create team button')
        self.click_close_icon()

    def verify_create_team_successfully(self, team_name):
        self.create_new_team(team_name)
        time.sleep(5)
        new_team_name = self.get_team_name()
        self.verify_text_match(new_team_name, team_name)
