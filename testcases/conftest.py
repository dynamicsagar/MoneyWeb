import os
import xlrd
import pytest
from selenium import webdriver

from base.webdriver_factory import WebDriverFactory
from pages.login.login_page import LoginPage
from utilities.util import Util


@pytest.fixture(scope="class")
def setUp():
    try:
        filePath = "./testdata/datasheet.xls"
        if os.path.exists(filePath):
            os.remove(filePath)
    except:
        print("Can not delete the file as it doesn't exists")

    folder_path = "./reports"
    # using listdir() method to list the files of the folder
    test = os.listdir(folder_path)
    for images in test:
        if images.endswith(".json") or images.endswith(".txt") or images.endswith(".png"):
            os.remove(os.path.join(folder_path, images))
        else:
            print("% s has been removed successfully" % folder_path)

    screenshot_path = "./screenshots"
    # using listdir() method to list the files of the folder
    test = os.listdir(screenshot_path)
    for images in test:
        if images.endswith(".png"):
            os.remove(os.path.join(screenshot_path, images))
        else:
            print("% s has been removed successfully" % screenshot_path)

    yield
    print("Running method level tearDown")


# @pytest.fixture(params=["chrome"], scope="function")
# # @pytest.fixture(scope="class")
# def oneTest(request):
#     remote_url = "http://localhost:4444/wd/hub"
#     if request.param == "chrome":
#         #     # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#         driver = webdriver.Remote(command_executor=remote_url, desired_capabilities={"browserName": "chrome"})
#
#     if request.param == "firefox":
#         # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#         driver = webdriver.Remote(command_executor=remote_url, desired_capabilities={"browserName": "firefox"})
#
#     if request.cls is not None:
#         request.cls.driver = driver
#     baseURL = "https://stageconsole.silamoney.com/login"
#     driver.get(baseURL)
#     driver.maximize_window()
#     yield driver
#     driver.quit()

@pytest.fixture(scope="class")
def oneTest(request, browser, env):
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance(env)

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running one time tearDown")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser, env):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance(env)
    utility = Util()
    lp = LoginPage(driver)

    # # Give the location of the file
    # loc = "./testdata/datasheet.xls"
    #
    # # To open Workbook
    # wb = xlrd.open_workbook(loc)
    # sheet = wb.sheet_by_index(0)
    # username = (sheet.cell_value(1, 0))

    # For row 0 and column 0

    username = utility.get_data(1)
    lp.verifyLoginSuccessfully(username, "Arcgate1!")
    # lp.verifyLoginSuccessfully("silaqa002@mailinator.com", "12345678")

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running one time tearDown")


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
