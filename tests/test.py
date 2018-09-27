from utils.login import Login
from utils.signout import SignOut
from config.configs import Configs
from time import sleep

Login().login(Configs.url, Configs.usr, Configs.pwd)
sleep(10)
SignOut().signOut()
Configs.drv.close()
exit()