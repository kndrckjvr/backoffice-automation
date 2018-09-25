from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep 

eml = "kendrickjaviercosca@gmail.com"
usr = "123456"

driver = webdriver.Chrome()
# Open site
driver.get("http://localhost/tsceressql/site/login")
print ("Opened Back Office")

# Click Forgot Password
driver.find_element_by_link_text('Forgot Password?').click()
sleep(1)

#Insert Usercode
elem = driver.find_element_by_id("Forgotpassword_E_MAIL")
elem.send_keys(usr)
print ("Usercode Entered") 
driver.find_element_by_id("apply").click()

sleep(1)
driver.find_element_by_xpath("//a[@data-value='E_MAIL']").click()
#Insert Email
elem = driver.find_element_by_id("Forgotpassword_E_MAIL")
elem.send_keys(eml)
print ("Email Entered")
driver.find_element_by_id("apply").click()
sleep(1)
#Go Back to Login Page
driver.find_element_by_xpath("//form[@id='yw0']//div//div[@class='btn-group']//a[@class='btn']").click()
sleep(4)
driver.close() 
print ("Done")
exit()
