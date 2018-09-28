from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from utils.login import Login
from utils.signout import SignOut
from utils.simulate import Simulate
from config.configs import Configs
from time import sleep

Login().login(Configs.url, Configs.usr, Configs.pwd)

Simulate().click_by_xpath("//ul[@class='sidebar-menu']//li[2]//a[@class='dropdown-toggle']")
print("Open Item Maintenance Dropdown")
Configs.drv.find_element_by_xpath("//ul[@class='sidebar-menu']//li[2]//ul//li[@id='menuitems']").click()

print("Menu Items Opened")

if Simulate().get_attribute_by_id("add", "disabled") == "disabled":
    print("Add Menu Item Opened")
else:
    Simulate().click_by_id("add")
    print("Add Menu Item Opened")
    sleep(1)

Simulate().click_by_xpath("//div[@id='department-opt']//select[@id='MenuItems_DEP_CODE']")

#SignOut().signOut(driver)

#exit()
