from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep 
from utils.opendriver import OpenDriver
from utils.signout import SignOut

class Login:
    def login(self, url, usr, pwd, driver):
        OpenDriver().openDriver(driver, url)

        Login().inputFields(usr, pwd, driver)        

        if driver.title == "Back Office - Login Site":
            elem = driver.find_element_by_id("LoginForm_password_em_")
            if "Incorrect user code or password." == elem.text:
                print(elem.text)
                driver.close()
                exit()    
            else:
                elem = driver.find_element_by_link_text("here").click()
                print("Pressed here link to Sign-in")
                sleep(1)
                SignOut().signOut(driver)
                Login().inputFields(usr, pwd, driver)

    def inputFields(self, usr, pwd, driver):
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys(usr)
        print ("Email Id entered") 

        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys(pwd)
        print ("Password entered")

        elem.send_keys(Keys.RETURN)
        sleep(1)