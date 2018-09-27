from utils.login import Login
from utils.signout import SignOut
from config.configs import Configs
from time import sleep

Login().login(Configs.url, Configs.usr, Configs.pwd, Configs.drv)
sleep(10)
SignOut().signOut(Configs.drv)
Configs.drv.close()
exit()