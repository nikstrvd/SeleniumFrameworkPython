import unittest
import pytest
import time
from Base.DriverClass import WebDriverClass
import Utilities.CustomLogger as cl
from Base.BasePage import BaseClass
from Pages.LoginPage import LoginPage
from Pages.DashBoardPage import DashBoardPage

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class DashboardPageDemoTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.lp = LoginPage(self.driver)
        self.bp = BaseClass(self.driver)
        self.dp = DashBoardPage(self.driver)

    def test_ChangePassword(self):
        self.lp.doLogin()
        self.lp.doClickLoginbutton()
        self.lp.doClickUserdropdown()
        self.dp.doAccessChangepassword()
        self.dp.doOldPassword()
        self.dp.doNewPassword()
        self.dp.doConfirmPassword()
        self.dp.doUpdateChangePassword()
        self.dp.doGetTextofValidationToastmsg()
