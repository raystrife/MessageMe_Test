import pytest
from base.webdriverfactory import WebDriverFactory

@pytest.yield_fixture()
def setUp():
    print("Running conftest demo setUp")
    yield
    print("Running conftest demo tearDown")

@pytest.yield_fixture(scope="class")
def oneTimeSetup(request, browser):
    print("Running conftest demo one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running conftest demo one time tearDown")

"""
Add the optional argument in the command line
"""
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

"""
Read the content for the optional argument
"""
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")