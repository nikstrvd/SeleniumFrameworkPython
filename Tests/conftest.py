import pytest
from Base.BasePage import BaseClass
from Base.DriverClass import WebDriverClass
import time


@pytest.fixture(scope='class')
def beforeClass(request):
    print('Before Class')
    driver1 = WebDriverClass()
    driver = driver1.getWebDriver("chrome")
    driver.maximize_window()
    bp = BaseClass(driver)
    bp.launchWebPage("http://backend.tmsapp.2stallions.site/login", "Login - TMS")
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print('After Class')


@pytest.fixture(scope='class')
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')
