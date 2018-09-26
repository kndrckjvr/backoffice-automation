from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from utils.login import Login
from utils.signout import SignOut
from config.configs import Configs
from time import sleep

Login().login(Configs.url, Configs.usr, Configs.pwd, Configs.drv)
driver = Configs.drv

print("Dashboard Opened")
driver.find_element_by_xpath("//ul[@class='sidebar-menu']//li[2]//a[@class='dropdown-toggle']").click()
driver.find_element_by_xpath("//ul[@class='sidebar-menu']//li[2]//ul//li[@id='menuitems']").click()
sleep(1)
print("Menu Items Opened")

driver.find_element_by_id('add').click()
sleep(1)
print("Add Menu Items Opened")

#driver.find_element_by_xpath("//div[@id='department-opt']//select[@id='MenuItems_DEP_CODE']").click()



# driver.find_element_by_xpath("//div[@id='department-opt']//div[@id='MenuItems_DEP_CODE_chzn']//span").click()

#SignOut().signOut(driver)

driver.close()
exit()
