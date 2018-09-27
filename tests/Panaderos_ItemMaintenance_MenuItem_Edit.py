from config.configs import Configs
from utils.login import Login
from utils.signout import SignOut
from utils.simulate import Simulate
from time import sleep

Login().login("http://cloud.jimac-inc.com/panadero", Configs.usr, Configs.pwd, Configs.drv)

print("Opened Dashboard")

Simulate().click_by_xpath(Configs.drv, "/html/body/div/aside/section/ul/li[2]/a")
Simulate().click_by_xpath(Configs.drv, "//*[@id='menuitems']/a")
print("Opened Menu Items")
sleep(1)

cont = True

while cont:

    Simulate().click_by_id(Configs.drv, "search")
    print("Opened Search Modal")
    sleep(1)

    while True:
        search_code=raw_input("Enter Search Code: ")
        Simulate().input_by_id(Configs.drv, "keyword", search_code)
        print("Entered Search Code " + search_code)
        sleep(1)
        print("Displayed Item with Search Code: " + search_code)
        if Configs.drv.find_element_by_xpath("//*[@id='menu-item_search']/div[1]/table/tbody/tr/td").text == "No results found.":
            print("No results found.")
        else:
            no_of_items=len(Configs.drv.find_elements_by_xpath("//*[@id='menu-item_search']/div[1]/table/tbody/tr[@class='can_be_selected']"))
            if no_of_items > 1:
                while True:
                    down=input("Enter how many down arrows? [1-"+str(no_of_items)+"] ")
                    if down <= no_of_items and down != 0:
                        Simulate().down_enter(Configs.drv, down)    
                        break
                    else:
                        print("Only "+str(no_of_items)+" are only available!")
            break
    
    Simulate().click_by_xpath(Configs.drv, "//*[@id='edit']")
    print("Opened Edit Item")
    sleep(1)

    Configs.drv.find_element_by_xpath("//*[@id='MenuItems_DR_DEF_QUANTITY']").clear()
    dr_qty = 0
    while dr_qty < 1 or dr_qty > 4294967295:
        dr_qty=input("Enter DR Quantity: ")
        if dr_qty < 1:
            print("Minimum is 1!")
            pass
        if dr_qty > 4294967295:
            print("Maximum is 4294967295!")
            pass
    Simulate().input_by_xpath(Configs.drv, "//*[@id='MenuItems_DR_DEF_QUANTITY']", dr_qty)
    print("Edited DR Default Quantity")
    Simulate().click_by_xpath(Configs.drv, "//*[@id='save']")
    sleep(1)

    while True:
        cont_input=raw_input("Continue?[Y/N]: ")
        if cont_input == "Y" or cont_input == 'y':
            cont = True
            break
        if cont_input == "N" or cont_input == 'n':
            cont = False
            break
        else:
            print("Error input!")
            pass
    

# for x in range(0, 74):
#     print(x)
#     print("Opened Menu Items")
#     Simulate().click_by_xpath(Configs.drv, "//*[@id='edit']")
#     sleep(1)

#     print("Opened Edit Menu Items")
#     Configs.drv.find_element_by_xpath("//*[@id='MenuItems_DR_DEF_QUANTITY']").clear()
#     Simulate().input_by_xpath(Configs.drv, "//*[@id='MenuItems_DR_DEF_QUANTITY']", "100")

#     print("Edited DR Default Quantity")
#     Simulate().click_by_xpath(Configs.drv, "//*[@id='save']")
#     sleep(1)

#     for y in range(0, x):
#         Simulate().click_by_xpath(Configs.drv, "//*[@id='content']/div[2]/div/div/div/ul/li[3]/a")
#         sleep(1)

SignOut().signOut(Configs.drv)

Configs.drv.close()
print("Browser Closed")
exit()