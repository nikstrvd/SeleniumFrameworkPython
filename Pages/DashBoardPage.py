from Base.BasePage import BaseClass
import Utilities.CustomLogger as cl

class DashBoardPage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #_menu = "//a[text()='"++"']" #xpath
    #_submenu = "//ul[@class='nav metismenu in mm-show']//i//following-sibling::span[text()='"++"']" #xpath
    #_submenu1 = "//ul[@class='nav metismenu in mm-show']//i//following-sibling::span[text()='"++"']/ancestor::a/following-sibling::ul/li/a[text()='"++"']" #xpath
    _changepassword = "//a[text()=' Change Password']" #xpath
    _oldpassword = "old_password" #id
    _newpassword = "new_password" #id
    _confirmnewpassword = "confirm_new_password" #id
    _updateprofile = ".btn.btn-primary.px-4.float-right" #css
    _cancelprofile = ".btn.btn-danger" #css
    _userdropdown = "(//span[@class='ml-1 nav-user-name hidden-sm'])[1]"  # xpath
    _toastmessage = "div.toast-message" #css

    def doAccessUserDropdown(self):
        self.clickOnElement(self._userdropdown, "xpath")
        cl.allureLogs("Click on UserLogged in Button from DashboardPage")

    def doAccessChangepassword(self):
        self.clickOnElement(self._changepassword, "xpath")
        cl.allureLogs("Click on Changepassword option from UserLogged in menu under Dashboard Page")

    def doOldPassword(self):
        self.sendText("123456", self._oldpassword, "id")
        cl.allureLogs("Enter Old password under Changepassword page from Dashboard Page")

    def doNewPassword(self):
        self.sendText("123456", self._newpassword, "id")
        cl.allureLogs("Enter New password under Changepassword page from Dashboard Page")

    def doConfirmPassword(self):
        self.sendText("123456", self._confirmnewpassword, "id")
        cl.allureLogs("Enter Confirm password under Changepassword page from Dashboard Page")

    def doUpdateChangePassword(self):
        self.clickOnElement(self._updateprofile, "css")
        cl.allureLogs("Click on Change Button in change password page from DashboardPage")

    def doCancelChangePassword(self):
        self.clickOnElement(self._cancelprofile, "css")
        cl.allureLogs("Click on Cancel Button in change password page from DashboardPage")

    def doGetTextofValidationToastmsg(self):
        validation = self.getText(self._toastmessage, "css")
        print(validation)
        cl.allureLogs("Verify Validation Text from Change Password Page")



