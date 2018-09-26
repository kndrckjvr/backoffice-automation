from selenium import webdriver

class OpenDriver:
    def openDriver(self, driver, url):
        driver.maximize_window()
        driver.get(url)
        print ("Opened Back Office") 