import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

s = Service(ChromeDriverManager().install())
s2 = Service(GeckoDriverManager().install())


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(service=s)
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=s2)
    else:
        driver = webdriver.Chrome(service=s)
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata['Project name'] = 'vkcom_pytest'
    config._metadata['Tester'] = 'NamigM'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
