from utils.login import Login
from utils.signout import SignOut
from utils.simulate import Simulate
from config.configs import Configs
from time import sleep

sim = Simulate()
Login().login(Configs.url, Configs.usr, Configs.pwd)
sleep(1)
print(sim.get_text_by_id("limit"))
sleep(10)
SignOut().signOut()
Configs.drv.close()
exit()