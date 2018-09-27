from config.configs import Configs
from time import sleep 
from utils.opendriver import OpenDriver
from utils.simulate import Simulate

# Open Browser
OpenDriver().openDriver(Configs.url)

# Click Forgot Password
Simulate().click_by_link("Forgot Password?")
sleep(1)

# Insert Usercode
Simulate().input_by_id("Forgotpassword_E_MAIL", Configs.usr)
print ("Usercode Entered") 
Simulate().click_by_id("apply")

# Switch to Email
sleep(1)
Simulate().click_by_xpath("//a[@data-value='E_MAIL']")

# Insert Email
Simulate().input_by_id("Forgotpassword_E_MAIL", Configs.eml)
print ("Email Entered")
Simulate().click_by_id("apply")
sleep(1)

# Go Back to Login Page
Simulate().click_by_xpath("//form[@id='yw0']//div//div[@class='btn-group']//a[@class='btn']")
sleep(1)
print ("Done")

# Close Browser
Configs.drv.close()

# Exit Python
exit()
