from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep 
from utils.login import Login
from utils.signout import SignOut
from config.configs import Configs
barcode = "57"

Login().login(Configs.url, Configs.usr, Configs.pwd, Configs.drv)
driver = Configs.drv
#Item Maintenance --> Menu Items
print("Entered Dashboard")
driver.find_element_by_xpath("//ul[@class='sidebar-menu']//li[2]//a[@class='dropdown-toggle']").click()
driver.find_element_by_xpath("//ul[@class='sidebar-menu']//li[2]//ul//li[@id='menuitems']").click()
sleep(1)



driver.find_element_by_id("search").click()
sleep(2)
elem = driver.find_element_by_id("keyword")
elem.send_keys(barcode)
print("Barcode " + barcode + " entered")
sleep(2)
elem.send_keys(Keys.ARROW_DOWN)
elem.send_keys(Keys.RETURN)
#elem = driver.find_element_by_xpath("//div[@id='menu-item_search']//div[@class='scrollableArea']//table//tbody//tr[1]").click() #//table//tbody//tr[1]
#print(elem.get_attribute("class"))
print ("Item Selected")
print ("Done")
SignOut().signOut(driver)

driver.close()
exit()
