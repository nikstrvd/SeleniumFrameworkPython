import time
from Base.DriverClass import WebDriverClass
import Utilities.CustomLogger as cl
from Base.BasePage import BaseClass
from Pages.LoginPage import LoginPage


wd = WebDriverClass()

driver = wd.getWebDriver("chrome")
bp = BaseClass(driver)
lp = LoginPage(driver)
driver.maximize_window()
bp.launchWebPage("http://backend.tmsapp.2stallions.site/login", "Login - TMS")
lp.doLogin()
lp.doClickLoginbutton()
lp.doClickUserdropdown()
lp.doClickLogoutbutton()
lp.doAccessForgetPasswordPage()
lp.enterTextinEmailfield()
lp.doClickResetbutton()
lp.doClickResetbutton()
lp.doClickLoginfromforgetpasswordpage()

#ele = bp.isElementDisplayed("email", "id")
#print(ele)
#bp.sendText("superadmin@mail.com", "email", "id")
#bp.sendText("123456", "password", "id")
#bp.clickOnElement("//button", "xpath")
#bp.clickOnElement("(//span[@class='ml-1 nav-user-name hidden-sm'])[1]", "xpath")
#bp.clickOnElement("(//a[normalize-space()='Logout'])[1]", "xpath")
time.sleep(2)
driver.quit()