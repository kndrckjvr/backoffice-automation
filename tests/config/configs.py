from selenium import webdriver

class Configs(object):
    # Browser Driver
    drv = webdriver.Chrome()

    # URL of the Login Page
    #url = "http://localhost/tsceressql/site/login"
    url = "http://192.168.0.70/tsceressql/site/login"

    # User Code
    usr = "000000"

    # Password
    pwd = "123"

    # Email
    eml = "kendrickjaviercosca@gmail.com"