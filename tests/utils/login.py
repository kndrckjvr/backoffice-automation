from config.configs import Configs
from time import sleep 
from utils.opendriver import OpenDriver
from utils.signout import SignOut
from utils.simulate import Simulate

class Login:
    # login Function
    # Function to Open and Login to the Login Page
    # params self url usr pwd
    # url ([URL] This is the url of the login page)
    # usr ([User Code] This is the user code of the user)
    # pwd ([Password] This is the password of the user)
    def login(self, url, usr, pwd):
        # Opening Browser
        OpenDriver().openDriver(url)

        # For User Inputs
        # usr = raw_input("Enter Usercode: ")
        # pwd = raw_input("Enter Password: ")

        # Input Fields
        Login().inputFields(usr, pwd)        

        # Error on inputs
        if Configs.drv.title == "Back Office - Login Site":
            # Scenario when the user has inserted wrong data
            if "Incorrect user code or password." == Configs.drv.find_element_by_id("LoginForm_password_em_").text:
                print(Configs.drv.find_element_by_id("LoginForm_password_em_").text)
                sleep(10)
                Configs.drv.close()
                exit()    
            # Scenario when the user is logged in to other ip address
            else:
                Simulate().click_by_link("here")
                print("Pressed here link to Sign-in")
                sleep(1)
                SignOut().signOut()
                Login().inputFields(usr, pwd)

    # inputFields Function
    # Function to Input the usercode and password of the user
    # params self usr pwd
    # usr ([User Code] This is the user code of the user)
    # pwd ([Password] This is the password of the user)
    def inputFields(self, usr, pwd):
        # Input User Code to the Field
        Simulate().input_by_id("LoginForm_username", usr)
        print ("Email Id entered")

        # Input Password to the Field
        Simulate().input_by_id("LoginForm_password", pwd)
        print ("Password entered")

        # Click Login Button
        Simulate().click_by_xpath("//form[@id='login-form']//div[3]//div[1]//button")
        sleep(1)