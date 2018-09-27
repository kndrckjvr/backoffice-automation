from config.configs import Configs
from selenium import webdriver

class OpenDriver:
    # openDriver Function
    # to open browser and enter login page
    # params url
    # url ([URL] This is the url of the login page)
    def openDriver(self, url):
        # Maximize Browser
        Configs.drv.maximize_window()

        # Set URL
        Configs.drv.get(url)
        print ("Opened Back Office") 