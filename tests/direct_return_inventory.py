from selenium.webdriver.common.keys import Keys
from utils.login import Login
from utils.signout import SignOut
from config.configs import Configs
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


Login().login(Configs.url, Configs.usr, Configs.pwd, Configs.drv)
driver = Configs.drv

print("Dashboard Opened")
driver.find_element_by_xpath("//ul[@class='sidebar-menu']//li[5]//a[@class='dropdown-toggle']").click()
sleep(1)
driver.find_element_by_xpath("//ul[@class='sidebar-menu']//li[5]//ul//li[@id='directreturn']").click()
print("Direct Receiving Opened")

elem = driver.find_element_by_id('add')
if elem.get_attribute("disabled") == "disabled":
    print("Add Direct Receiving Opened")
else:
    elem.click()
    print("Add Direct Receiving Opened")
    sleep(1)

driver.find_element_by_xpath("//div[@id='DirectReturn_SUP_CODE_chzn']").click()
driver.find_element_by_xpath("//div[@id='DirectReturn_SUP_CODE_chzn']//div[@class='chzn-drop']//ul[@class='chzn-results']//li[@id='DirectReturn_SUP_CODE_chzn_o_0']").click()
print("Added Supplier")
sleep(1)
driver.find_element_by_xpath("//div[@id='DirectReturn_LOC_CODE_chzn']").click()
driver.find_element_by_xpath("//div[@id='DirectReturn_LOC_CODE_chzn']//div[@class='chzn-drop']//ul[@class='chzn-results']//li[@id='DirectReturn_LOC_CODE_chzn_o_0']").click()
print("Added Location")

elem = driver.find_element_by_xpath("//table[@id='DataTables_Table_0']//tbody[@class='myDatatableClass']//tr[@class='odd']//td") #[0]
driver.execute_script("arguments[0].click();", elem)
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.send_keys(Keys.ENTER)
actions.perform()
print("Search Modal Opened")
sleep(3)
actions = ActionChains(driver)
actions.send_keys(Keys.DOWN)
actions.send_keys(Keys.ENTER)
actions.perform()
print("First Item Selected")

# driver.find_element_by_xpath("//div[@id='DirectReturn_BRN_CODE_chzn']").click()
# driver.find_element_by_xpath("//div[@id='DirectReturn_BRN_CODE_chzn']//div[@class='chzn-drop']//ul[@class='chzn-results']//li[@id='DirectReturn_BRN_CODE_chzn_o_1']").click()
# print("Added Branch")

elem = driver.find_element_by_id("save")
driver.execute_script("arguments[0].click();", elem)
print("Save")

sleep(3)
driver.find_element_by_xpath("//html//body//div[3]//div//div//div[2]//button[2]").click()
# //*[@id="post"]
sleep(1)
SignOut().signOut(driver)
driver.close()
exit()
