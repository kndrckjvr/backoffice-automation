from selenium.webdriver.common.keys import Keys
from utils.login import Login
from utils.signout import SignOut
from config.configs import Configs
from time import sleep

Login().login(Configs.url, Configs.usr, Configs.pwd, Configs.drv)
driver = Configs.drv

print("Dashboard Opened")
driver.find_element_by_xpath("//ul[@class='sidebar-menu']//li[5]//a[@class='dropdown-toggle']").click()
driver.find_element_by_xpath("//ul[@class='sidebar-menu']//li[5]//ul//li[@id='directreceiving']").click()
sleep(1)
print("Direct Receiving Opened")

elem = driver.find_element_by_id('add')
if elem.get_attribute("disabled") == "disabled":
    print("Add Direct Receiving Opened")
else:
    elem.click()
    print("Add Direct Receiving Opened")
    sleep(1)
driver.
driver.find_element_by_xpath("//div[@id='DirectReceiving_BRN_CODE_chzn']").click()
driver.find_element_by_xpath("//div[@id='DirectReceiving_BRN_CODE_chzn']//div[@class='chzn-drop']//ul[@class='chzn-results']//li[@id='DirectReceiving_BRN_CODE_chzn_o_1']").click()
print("Added Branch")
driver.find_element_by_xpath("//div[@id='DirectReceiving_DES_CODE_chzn']").click()
driver.find_element_by_xpath("//div[@id='DirectReceiving_DES_CODE_chzn']//div[@class='chzn-drop']//ul[@class='chzn-results']//li[@id='DirectReceiving_DES_CODE_chzn_o_1']").click()
print("Added Location")
driver.find_element_by_xpath("//div[@id='DirectReceiving_SUP_CODE_chzn']").click()
driver.find_element_by_xpath("//div[@id='DirectReceiving_SUP_CODE_chzn']//div[@class='chzn-drop']//ul[@class='chzn-results']//li[@id='DirectReceiving_SUP_CODE_chzn_o_1']").click()
print("Added Supplier")
driver.find_element_by_xpath("//table[@id='DataTables_Table_0']//tbody//tr[@class='odd']//td[1]").click()
#print("Add Menu Items Opened")

#driver.find_element_by_xpath("//div[@id='department-opt']//select[@id='MenuItems_DEP_CODE']").click()



# driver.find_element_by_xpath("//div[@id='department-opt']//div[@id='MenuItems_DEP_CODE_chzn']//span").click()

#SignOut().signOut(driver)
sleep(10)
driver.close()
exit()
