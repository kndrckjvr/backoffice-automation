from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

class SignOut:
    def signOut(self, driver):
        sleep(1)
        elem = driver.find_element_by_xpath("//nav//div[@class='navbar-custom-menu']//ul//li//a").click()
        print("Opened Account Dropdown")
        sleep(1)
        elem = driver.find_element_by_xpath("//nav//div[@class='navbar-custom-menu']//ul//li//ul//li//div[@class='pull-right']//a").click()
        print("Signed out")
        sleep(1)
