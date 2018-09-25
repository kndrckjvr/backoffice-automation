from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep 

usr = "000000"
pwd = "123"

driver = webdriver.Chrome()
# or you can use Chrome(executable_path="/usr/bin/chromedriver")
driver.get("http://localhost/tsceressql/site/login")
print ("Opened Back Office") 


elem = driver.find_element_by_id("LoginForm_username")
elem.send_keys(usr)
print ("Email Id entered") 

elem = driver.find_element_by_id("LoginForm_password")
elem.send_keys(pwd)
print ("Password entered")

elem.send_keys(Keys.RETURN)
sleep(2)

#Item Maintenance --> Menu Items
#elem = driver.find_element_by_xpath("//ul[@class='sidebar-menu']//li[2]//a[@class='dropdown-toggle']").click()
#sleep(1)
#elem = driver.find_element_by_xpath("//ul[@class='sidebar-menu']//li[2]//ul//li[@id='menuitems']").click()

elem = driver.find_element_by_xpath("//nav//div[@class='navbar-custom-menu']//ul//li//a").click()
print("Opened Account Dropdown")
sleep(1)
elem = driver.find_element_by_xpath("//nav//div[@class='navbar-custom-menu']//ul//li//ul//li//div[@class='pull-right']//a").click()
print("Signed out")
sleep(1)
driver.close() 
print ("Done") 
exit()
