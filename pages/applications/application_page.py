import time

from base.selenium_driver import SeleniumDriver
from testcases.message import *


class CreateAPP(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _application_page_heading = "//span[contains(text(),'Application Detail')]"
    _hosted_api_demo_link = "//a[contains(text(),'hosted API explorer')]"
    _you_do_not_have_app_yet_text = "//p[contains(text(),'You do not have any apps yet.')]"
    _create_app_button = "//button[contains(text(),'Create your first app now!')]"
    
    # step 1 - Name your App
    _step_one_heading = "//h2[contains(text(),'App Pending')]"
    _close_icon = "//span[contains(text(),'×')]"
    _step_one_sub_heading = "//h2[contains(text(),'Create an internal and public name for your app.')]"
    _step_one_description = "//p[contains(text(),'The internal app name will be what you see within ')]"
    _app_name_field = "//input[@id='createAppForm.name']"
    _public_app_name_field = "//input[@id='createAppForm.brand_name']"
    _continue_button = "//button[contains(text(),'Continue')]"
    
    # step 2 - Create a Handle
    _step_second_heading = "//h2[contains(text(),'Give your app a handle.')]"
    _app_handle_field = "//input[@id='createAppForm.handle']"
    _empty_app_handle_message = '''//div[contains(text(),"Can't use spaces or special characters.")]'''
    
    # step 3 - Generate tePublic Eth address
    _step_third_heading = "//h2[contains(text(),'Generate a public Ethereum address, or provide us ')]"
    _step_third_description_text = "//p[contains(text(),'Dow')]"
    _generate_address_field = "//input[@id='keyGenForm.address']"
    _generate_button = "//button[contains(text(),'Generate')]"

    def get_application_page_heading(self):
        self.wait_for_element(self._application_page_heading)
        return self.get_text(self._application_page_heading)

    def click_demo_link(self):
        self.element_click(self._hosted_api_demo_link)

    def get_no_app_text(self):
        return self.get_text(self._you_do_not_have_app_yet_text)

    def click_create_app_button(self):
        self.element_click(self._create_app_button)

    def get_step1_heading(self):
        return self.get_text(self._step_one_heading)

    def get_step1_subheading(self):
        return self.get_text(self._step_one_sub_heading)

    def get_step1_description(self):
        return self.get_text(self._step_one_description)

    def enter_app_name(self, app_name):
        self.element_click(self._app_handle_field)
        self.send_keys(self._app_handle_field, app_name)

    def enter_public_app_name(self, public_app_name):
        self.element_click(self._public_app_name_field)
        self.send_keys(self._public_app_name_field, public_app_name)

    def click_continue_button(self):
        self.element_click(self._continue_button)

    def get_step2_heading(self):
        return self.get_text(self._step_second_heading)

    def enter_app_handle(self, app_handle):
        self.element_click(self._app_handle_field)
        self.send_keys(self._app_handle_field)

    def get_step3_heading(self):
        return self.get_text(self._step_third_heading)

    def get_step3_description(self):
        return self.get_text(self._step_third_description_text)

    def enter_eth_address(self):
        self.element_click(self._generate_address_field)
        self.send_keys(self._generate_address_field)

    def click_generate_button(self):
        self.element_click(self._generate_button)

    def verify_application_heading(self):
        text = self.get_application_page_heading()
        self.verify_text_contains(text, APPLICATION_HEADING)
