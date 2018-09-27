from config.configs import Configs
from time import sleep
from utils.simulate import Simulate

class SignOut:
    # signOut Function
    # signout user using account dropdown
    def signOut(self):
        sleep(1)
        
        # Click Account Dropdown
        Simulate().click_by_xpath("//nav//div[@class='navbar-custom-menu']//ul//li//a")
        print("Opened Account Dropdown")
        sleep(1)

        # Click Sign out Button
        Simulate().click_by_xpath("//nav//div[@class='navbar-custom-menu']//ul//li//ul//li//div[@class='pull-right']//a")
        print("Signed out")
        sleep(1)
