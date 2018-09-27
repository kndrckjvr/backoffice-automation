from config.configs import Configs
from utils.login import Login
from utils.signout import SignOut
from utils.simulate import Simulate
from time import sleep

# Login to Login Page
Login().login(Configs.url, Configs.usr, Configs.pwd)

# Dashboard Opened
print("Dashboard Opened")


# Opening side menu Item Maintenance
Simulate().click_by_xpath("/html/body/div/aside/section/ul/li[5]/a")
# Opening side menu Item Maintenance's Menu Items
Simulate().click_by_xpath("//*[@id='directreturn']/a")
print("Opened Direct Return")
sleep(1)

# Checking if Add Button is disabled
elem = Configs.drv.find_element_by_id('add')
if elem.get_attribute("disabled") == "disabled":
    print("Add Direct Receiving Opened")
else:
    elem.click()
    print("Add Direct Receiving Opened")
    sleep(1)

Simulate().click_by_xpath("//div[@id='DirectReturn_SUP_CODE_chzn']")
Simulate().click_by_xpath("//div[@id='DirectReturn_SUP_CODE_chzn']//div[@class='chzn-drop']//ul[@class='chzn-results']//li[@id='DirectReturn_SUP_CODE_chzn_o_0']")
print("Added Supplier")
sleep(1)

Configs.drv.find_element_by_xpath("//div[@id='DirectReturn_LOC_CODE_chzn']").click()
Configs.drv.find_element_by_xpath("//div[@id='DirectReturn_LOC_CODE_chzn']//div[@class='chzn-drop']//ul[@class='chzn-results']//li[@id='DirectReturn_LOC_CODE_chzn_o_0']").click()
print("Added Location")

elem = Configs.drv.find_element_by_xpath("//table[@id='DataTables_Table_0']//tbody[@class='myDatatableClass']//tr[@class='odd']//td") #[0]
Configs.drv.execute_script("arguments[0].click();", elem)
actions = ActionChains(Configs.drv)
actions.send_keys(Keys.ENTER)
actions.send_keys(Keys.ENTER)
actions.perform()
print("Search Modal Opened")
sleep(3)
actions = ActionChains(Configs.drv)
actions.send_keys(Keys.DOWN)
actions.send_keys(Keys.ENTER)
actions.perform()
print("First Item Selected")

# Configs.drv.find_element_by_xpath("//div[@id='DirectReturn_BRN_CODE_chzn']").click()
# Configs.drv.find_element_by_xpath("//div[@id='DirectReturn_BRN_CODE_chzn']//div[@class='chzn-drop']//ul[@class='chzn-results']//li[@id='DirectReturn_BRN_CODE_chzn_o_1']").click()
# print("Added Branch")

elem = Configs.drv.find_element_by_id("save")
Configs.drv.execute_script("arguments[0].click();", elem)
print("Save")

sleep(3)
elem = Configs.drv.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/button[2]")
Configs.drv.execute_script("arguments[0].click();", elem)
elem = Configs.drv.find_element_by_xpath("//*[@id='post']")
Configs.drv.execute_script("arguments[0].click();", elem)
elem = Configs.drv.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/button[1]")
Configs.drv.execute_script("arguments[0].click();", elem)
# //*[@id="post"]
# sleep(1)
# SignOut().signOut()
# Configs.drv.close()
# exit()
