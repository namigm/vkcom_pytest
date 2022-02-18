import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

s1 = Service(ChromeDriverManager().install())
s2 = Service(GeckoDriverManager().install())


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox(GeckoDriverManager().install())
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver


def pytest_addoption(parser):  # value from CLI
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # return the Browser to setup method
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata['Project name'] = 'vkcom_pytest'
    config._metadata['Tester'] = 'NamigM'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

