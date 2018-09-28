from config.configs import Configs
from utils.login import Login
from utils.signout import SignOut
from utils.simulate import Simulate
from time import sleep

# Login to Login Page
Login().login("http://cloud.jimac-inc.com/panadero", Configs.usr, Configs.pwd)

# Dashboard Opened
print("Opened Dashboard")

# Opening side menu Item Maintenance
Simulate().click_by_xpath("/html/body/div/aside/section/ul/li[2]/a")
# Opening side menu Item Maintenance's Menu Items
Simulate().click_by_xpath("//*[@id='menuitems']/a")
print("Opened Menu Items")
sleep(1)

cont = True
# Multiple Searches
while cont:
    
    # Clicking Search Button
    Simulate().click_by_id("search")
    print("Opened Search Modal")
    sleep(1)

    while True:
        # Receiving Input of User
        search_code=raw_input("Enter Search Code: ")
        # Insert the Data
        Simulate().input_by_id("keyword", search_code)
        print("Entered Search Code " + search_code)
        sleep(1)

        # Display Results
        print("Displayed Item with Search Code: " + search_code)
        # Checking Results
        if Simulate().get_text_by_xpath("//*[@id='menu-item_search']/div[1]/table/tbody/tr/td") == "No results found.":
            print("No results found.")
        else:
            no_of_items=len(Simulate().get_elements_by_xpath("//*[@id='menu-item_search']/div[1]/table/tbody/tr[@class='can_be_selected']"))
            if no_of_items > 1:
                while True:
                    down=input("Enter how many down arrows? [1-"+str(no_of_items)+"] ")
                    if down <= no_of_items and down != 0:
                        # Selecting the Item and Displaying
                        Simulate().down_enter(down)    
                        break
                    else:
                        print("Only "+str(no_of_items)+" are only available!")
            break
    
    # Clicking Edit Button
    Simulate().click_by_xpath("//*[@id='edit']")
    print("Opened Edit Item")
    sleep(1)

    # Checking the inputs
    dr_qty = 0
    while dr_qty < 1 or dr_qty > 4294967295:
        dr_qty=input("Enter DR Quantity: ")
        if dr_qty < 1:
            print("Minimum is 1!")
            pass
        if dr_qty > 4294967295:
            print("Maximum is 4294967295!")
            pass

    # Insert the Data
    Simulate().input_by_xpath("//*[@id='MenuItems_DR_DEF_QUANTITY']", dr_qty)
    print("Edited DR Default Quantity")

    # Click Save Button
    Simulate().click_by_xpath("//*[@id='save']")
    sleep(1)

    # Exit Condition
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
    
# //Prototype//
# for x in range(0, 74):
#     print(x)
#     print("Opened Menu Items")
#     Simulate().click_by_xpath("//*[@id='edit']")
#     sleep(1)

#     print("Opened Edit Menu Items")
#     Configs.drv.find_element_by_xpath("//*[@id='MenuItems_DR_DEF_QUANTITY']").clear()
#     Simulate().input_by_xpath("//*[@id='MenuItems_DR_DEF_QUANTITY']", "100")

#     print("Edited DR Default Quantity")
#     Simulate().click_by_xpath("//*[@id='save']")
#     sleep(1)

#     for y in range(0, x):
#         Simulate().click_by_xpath("//*[@id='content']/div[2]/div/div/div/ul/li[3]/a")
#         sleep(1)

# Signout
SignOut().signOut()

# Browser Closing
Configs.drv.close()
print("Browser Closed")

# Exit Python
exit()