from selenium import webdriver
from time import sleep 
from utils.opendriver import OpenDriver
from utils.signout import SignOut
from utils.simulate import Simulate

class Login:
    def login(self, url, usr, pwd, driver):
        #Opening Drivers
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
        Simulate().input_by_id(driver, "LoginForm_username", usr)
        print ("Email Id entered")

        Simulate().input_by_id(driver, "LoginForm_password", pwd)
        print ("Password entered")

        Simulate().click_by_xpath(driver, "//form[@id='login-form']//div[3]//div[1]//button")
        sleep(1)