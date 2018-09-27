from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep 
from utils.login import Login
from utils.signout import SignOut
from config.configs import Configs

Login().login(Configs.url, Configs.usr, Configs.pwd, Configs.drv)
print("Opened Dashboard")

Simulate().click_by_xpath(Configs.drv, "/html/body/div/aside/section/ul/li[2]/a")
Simulate().click_by_xpath(Configs.drv, "//*[@id='menuitems']/a")
print("Opened Menu Items")
sleep(1)

Simulate().click_by_id(Configs.drv, "search")
print("Opened Search Modal")
sleep(1)

while True:
    search_code=raw_input("Enter Search Code: ")
    Simulate().input_by_id(Configs.drv, "keyword", search_code)
    print("Entered Search Code " + search_code)
    sleep(1)
    if Configs.drv.find_element_by_xpath("//*[@id='menu-item_search']/div[1]/table/tbody/tr/td").text == "No results found.":
        print("No results found.")
    else:
        Simulate().down_enter(Configs.drv, 1)
        print ("Item Selected")
        break

print("Done")
SignOut().signOut(Configs.drv)
Configs.drv.close()
print("Browser Closed")
exit()
