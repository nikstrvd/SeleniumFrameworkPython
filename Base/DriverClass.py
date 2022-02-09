from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import Utilities.CustomLogger as cl

class WebDriverClass:
    log = cl.customLogger()

    def getWebDriver(self, browserName):
        driver = None
        if browserName == "chrome":
            s = Service('C:/Users/2Stallions/PycharmProjects/SeleniumFrameworkPython/Drivers/chromedriver.exe')
            driver = webdriver.Chrome(service=s)
            self.log.info("Chrome Driver is initializing")
        elif browserName == "ie":
            driver = webdriver.Ie(executable_path="C:/Users/2Stallions/PycharmProjects/SeleniumFrameworkPython/Drivers/IEDriverServer.exe")
            self.log.info("Ie Driver is initializing")
        elif browserName == "firefox":
            driver = webdriver.Firefox(executable_path="C:/Users/2Stallions/PycharmProjects/SeleniumFrameworkPython/Drivers/geckodriver.exe")
            self.log.info("FireFox Driver is initializing")
        elif browserName == "edge":
            driver = webdriver.Edge(executable_path="C:/Users/2Stallions/PycharmProjects/SeleniumFrameworkPython/Drivers/msedgedriver.exe")
            self.log.info("Edge Driver is initializing")

        return driver
