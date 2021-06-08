import os

import pytest

from base.webdriver_factory import WebDriverFactory
# from pages.test001_login_page import LoginPage
from testcases.test_config import *


@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser, env):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance(env)
    # lp = LoginPage(driver)

    # # Give the location of the file
    # loc = ("testcases\login.xls")
    #
    # # To open Workbook
    # wb = xlrd.open_workbook(loc)
    # sheet = wb.sheet_by_index(0)

    # For row 0 and column 0
    # username = (sheet.cell_value(1, 0))
    # password = (sheet.cell_value(1, 1))
    # username = user_email
    # user_pass = password
    # lp.login_to_website(username, user_pass)

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running one time tearDown")


@pytest.yield_fixture(scope="class")
def remove_files():
    folder_path = ("./reports")
    # using listdir() method to list the files of the folder
    test = os.listdir(folder_path)
    for images in test:
        if images.endswith(".json") or images.endswith(".txt") or images.endswith(".png"):
            os.remove(os.path.join(folder_path, images))


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")
    parser.addoption("--env", help="Type of environment i.e prod, qa, dev")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")


@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")
