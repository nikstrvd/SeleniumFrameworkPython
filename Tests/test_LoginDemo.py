import unittest
import pytest
import time
from Base.DriverClass import WebDriverClass
import Utilities.CustomLogger as cl
from Base.BasePage import BaseClass
from Pages.LoginPage import LoginPage

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class LoginPageDemoTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.lp = LoginPage(self.driver)
        self.bp = BaseClass(self.driver)

    def test_LoginPage(self):
        self.lp.doLogin()
        self.lp.doClickLoginbutton()
        self.lp.doClickUserdropdown()
        self.lp.doClickLogoutbutton()

    def test_ForgetpasswordPage(self):
        self.lp.doAccessForgetPasswordPage()
        self.lp.enterTextinEmailfield()
        self.lp.doClickResetbutton()
        self.lp.doClickResetbutton()
        self.lp.doClickLoginfromforgetpasswordpage()

