from config.configs import Configs
from utils.login import Login
from utils.signout import SignOut
from utils.simulate import Simulate

Login().login(Configs.url, Configs.usr, Configs.pwd)
# Entered Dashboard
print("Opened Dashboard")

# Open Inventory
Simulate().click_by_xpath("/html/body/div/aside/section/ul/li[5]/a")
# Open Inventory Reports
Simulate().click_by_xpath("//*[@id='Reports2']/a")
# Open Direct Receiving
Simulate().click_by_xpath("//*[@id='Directreceivingreport']/a")

SignOut().signOut()

# Start Date
# End Date
# Report Type
# Supplier Department Branch
# View