from Base.BasePage import BaseClass
import Utilities.CustomLogger as cl


class LoginPage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _email = "email" #id
    _password = "password" #id
    _loginbutton = "//button" #xpath
    _userdropdown = "(//span[@class='ml-1 nav-user-name hidden-sm'])[1]" #xpath
    _logoutbutton = "(//a[normalize-space()='Logout'])[1]" #xpath
    _forgetpasswordlink = "(//a[normalize-space()='Forgot password?'])[1]" #xpath
    _getValidationmsg = "//li" #xpath
    _loginfromforgetpassword = ".text-primary.ml-2" #css

    def doLogin(self):
        self.sendText("superadmin@mail.com", self._email, "id")
        self.sendText("123456", self._password, "id")
        cl.allureLogs("Entered Username & Password in LoginPage")

    def doClickLoginbutton(self):
        self.clickOnElement(self._loginbutton, "xpath")
        cl.allureLogs("Click on Login Button from LoginPage")

    def doClickUserdropdown(self):
        self.clickOnElement(self._userdropdown, "xpath")
        cl.allureLogs("Click on UserLogged in Button from DashboardPage")

    def doClickLogoutbutton(self):
        self.clickOnElement(self._logoutbutton, "xpath")
        cl.allureLogs("Click on Loout Button from DashboardPage")

    def doAccessForgetPasswordPage(self):
        self.clickOnElement(self._forgetpasswordlink, "xpath")
        cl.allureLogs("Click on Forget Password Link from LoginPage")

    def enterTextinEmailfield(self):
        self.sendText("testing@mail.com", self._email, "id")
        cl.allureLogs("Enter Email id under Forget Password Page")

    def doClickResetbutton(self):
        self.clickOnElement(self._loginbutton, "xpath")
        cl.allureLogs("Click on Reset Button from Forget Password Page")

    def doGetTextofValidation(self):
        validation = self.getText(self._getValidationmsg, "xpath")
        cl.allureLogs("Verify Validation Text from Forget Password Page")

    def doClickLoginfromforgetpasswordpage(self):
        self.clickOnElement(self._loginfromforgetpassword, "css")
        cl.allureLogs("Click on Login Button from Forget Password Page")



